from keras.models import Model
import numpy as np
import pandas as pd
from utils import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
from DataBaseManager import DataBaseManager

from Recommendation_Model import RecommenderModel, EmbeddingLayer

class RecommendationModelManager():
    def __init__(self, modelName="recommendation_model"):
        self.model = load_model(modelName)
        self.modelName = modelName
    
    def save_model(self,modelName):
        self.model.save(modelName)
    
    def update_model(self):
        try:
            dbManager = DataBaseManager()
            reviews_data = dbManager.get_reviews_data()
            user_enc = LabelEncoder()
            reviews_data['user'] = user_enc.fit_transform(reviews_data['user_id'])
            n_users = reviews_data['user'].nunique()

            item_enc = LabelEncoder()
            reviews_data['restaurant'] = item_enc.fit_transform(reviews_data['business_id'])
            n_restaurant = reviews_data['restaurant'].nunique()

            reviews_data['stars'] = reviews_data['stars'].values.astype(np.float32)
            min_rating = min(reviews_data['stars'])
            max_rating = max(reviews_data['stars'])
            n_users, n_restaurant, min_rating, max_rating


            X = reviews_data[['user', 'restaurant']].values
            y = reviews_data['stars'].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

            n_factors = 50
            X_train_array = [X_train[:, 0], X_train[:, 1]]
            X_test_array = [X_test[:, 0], X_test[:, 1]]

            model = RecommenderModel(n_users, n_restaurant, n_factors, min_rating, max_rating)
            print(model.summary())

            model.fit(x=X_train_array, y=y_train, batch_size=64, epochs=5,verbose=1, validation_data=(X_test_array, y_test))
            
            self.model = model
            self.save_model(self.modelName)
            dbManager.update_recommendation_model_data(reviews_data, n_restaurant)
            return True
        except:
          return False

    def get_model(self):
        return self.model

    def get_recommendations(self,userModelID, restuarantsData, range=50):
        restaurantsToPredict = restuarantsData[~np.isnan(restuarantsData['model_id'])]
        restaurantsModelIDList = restaurantsToPredict['model_id']
        predictionMatrix = [np.array(len(restaurantsModelIDList) * [userModelID]),restaurantsModelIDList]
        predictedRatings = self.model.predict_on_batch(predictionMatrix)
        recommendedUserRatings = pd.DataFrame({'business_id':restaurantsToPredict['business_id'].values,'star': predictedRatings.flatten()})
        return recommendedUserRatings.sort_values(by='star',ascending=False)['business_id'][0:range]
