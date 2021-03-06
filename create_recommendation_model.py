import numpy as np
import sqlite3 as sql
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model

from Recommendation_Model import RecommenderModel, EmbeddingLayer

conn = sql.connect('RecommendationsDB.db')
c = conn.cursor()

reviews_data = pd.read_sql('SELECT * FROM reviews', conn)

reviews_data.head()

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
X_train.shape, X_test.shape, y_train.shape, y_test.shape

n_factors = 50
X_train_array = [X_train[:, 0], X_train[:, 1]]
X_test_array = [X_test[:, 0], X_test[:, 1]]

model = RecommenderModel(n_users, n_restaurant, n_factors, min_rating, max_rating)
print(model.summary())

history = model.fit(x=X_train_array, y=y_train, batch_size=64, epochs=5,verbose=1, validation_data=(X_test_array, y_test))


model.save("recommendation_model") # save model to file


#insert multiple records in a single query
for i in range(n_restaurant):
    query = "UPDATE restuarants SET model_id = {} WHERE business_id='{}'".format(reviews_data['restaurant'][i], reviews_data['business_id'][i])
    c.execute(query)
for i in range(n_restaurant):
    query = "UPDATE users SET model_id = {} WHERE user_id='{}'".format(reviews_data['user'][i], reviews_data['user_id'][i])
    c.execute(query)

#commit the changes to db			
conn.commit()
#close the connection
conn.close()
