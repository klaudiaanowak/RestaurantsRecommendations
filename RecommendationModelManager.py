from keras.models import Model
import numpy as np
import pandas as pd
from keras.models import load_model

class RecommendationModelManager():
    def __init__(self, modelName="recommendation_model"):
        self.model = load_model("recommendation_model")
    
    def save_model(self,modelName):
        self.model.save(modelName)
    
    def update_model(self):
        self.model = None

    def get_model():
        return self.model

    def get_recommendations(self,userModelID, restuarantsData, range=50):
        restaurantsToPredict = restuarantsData[~np.isnan(restuarantsData['model_id'])]
        restaurantsModelIDList = restaurantsToPredict['model_id']
        predictionMatrix = [np.array(len(restaurantsModelIDList) * [userModelID]),restaurantsModelIDList]
        predictedRatings = self.model.predict_on_batch(predictionMatrix)
        recommendedUserRatings = pd.DataFrame({'business_id':restaurantsToPredict['business_id'].values,'star': predictedRatings.flatten()})
        return recommendedUserRatings.sort_values(by='star',ascending=False)['business_id'][0:range]
