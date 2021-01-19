import sqlite3 as sql
import pandas as pd
import random
import uuid
from datetime import datetime

class DataBaseManager():
    def __init__(self, dbName='RecommendationsDB.db'):
        self.conn = sql.connect(dbName)
        self.c = self.conn.cursor()
        self.user = None
        
    def login_user(self, username, password):
        if(username is "" or password is ""):
            return False
        query = "SELECT * FROM users WHERE user_id = '{}' and haslo = '{}'".format(username, password)
        user_data = pd.read_sql(query, self.conn)
        if len(user_data) > 0:
            self.user = user_data
            return True
        return False

    def register_user(self,userName,password, name, email, tel):
        if(userName is "" or password is "" or name is ""):
            return False
        query = "SELECT * FROM users WHERE user_id = '{}'".format(userName)
        user_data = pd.read_sql(query, self.conn)
        if len(user_data) > 0:
            return False
        try:
            self.c.execute('INSERT INTO  users (user_id, haslo, name, email, telefon) VALUES(?,?,?,?,?)',(userName, password, name, email, tel))
            self.conn.commit() 
            return True
        except:
            return False

    def get_user_modelID(self):
        return self.user['model_id'].values[0]

    def get_user_name(self):
        return self.user['name'].values[0]

    def get_restuarant_data(self):
        return pd.read_sql('SELECT * FROM restuarants WHERE model_id', self.conn)
 
    def get_restuarant_data_with_text(self, search_name):
        return pd.read_sql("SELECT * FROM restuarants WHERE name LIKE ('%{}%') GROUP BY name".format(search_name), self.conn)
               
    def get_default_recommended_restaurants(self):
        query ='SELECT name, categories, stars FROM restuarants WHERE categories is not null ORDER BY stars DESC'
        recommendationData = pd.read_sql(query, self.conn)
        return recommendationData

    def get_recommended_restaurants(self,recommendedModelIDs):
        query ='SELECT name, categories, stars FROM restuarants WHERE business_id IN {}'.format(list(recommendedModelIDs.values)).replace("[","(").replace("]",")")
        recommendationData = pd.read_sql(query, self.conn)
        return recommendationData
    
    def get_reviews_data(self):
        reviews_data = pd.read_sql('SELECT * FROM reviews', self.conn)
        return reviews_data

    def update_recommendation_model_data(self, reviews_data, n_restaurant):
        for i in range(n_restaurant):
            query = "UPDATE restuarants SET model_id = {} WHERE business_id='{}'".format(reviews_data['restaurant'][i], reviews_data['business_id'][i])
            self.c.execute(query)
        for i in range(n_restaurant):
            query = "UPDATE users SET model_id = {} WHERE user_id='{}'".format(reviews_data['user'][i], reviews_data['user_id'][i])
            self.c.execute(query)

        self.conn.commit()
    
    def add_rating(self, business_id, grade):
        if(grade<1 or grade>5):
            return False
        review_id = uuid.uuid4()
        user_id = self.user['user_id'].values[0]
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        print(business_id)
        print(user_id)
        print(review_id)
        print(grade)
        print(dt_string)
        query = "INSERT INTO  reviews (review_id, user_id, business_id, stars, date) VALUES('{}','{}','{}',{},'{}')".format(review_id,user_id,business_id,grade,dt_string)
        print(query)
        self.c.execute(query)
        self.conn.commit() 
        return True
  
