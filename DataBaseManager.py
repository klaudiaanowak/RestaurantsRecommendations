import sqlite3 as sql
import pandas as pd

class DataBaseManager():
    def __init__(self, dbName='RecommendationsDB.db'):
        self.conn = sql.connect(dbName)
        self.c = self.conn.cursor()
        self.user = None
        
    def login_user(self, username, password):
        if(username is ""):
            return False
        query = "SELECT * FROM users WHERE user_id='{}'".format(username)
        user_data = pd.read_sql(query, self.conn)
        if len(user_data) > 0:
            # if user_data['password'] == password:
            if True: # TODO: to change - set the condition
                self.user = user_data
                return True
        return False
    def register_user(self,userName,password, name, email, tel):
        try:
            self.c.execute('INSERT INTO  users (login, haslo, name, email, tel) VALUES(?,?,?,?,?)',(userName, password, name, email, tel))
            self.conn.commit() 
            return True
        except:
            return False

    def get_user_modelID(self):
        return self.user['model_id']

    def get_user_name(self):
        return self.user['name'].values[0]

    def get_restuarant_data(self):
        return pd.read_sql('SELECT * FROM restuarants WHERE model_id', self.conn)
        
    def get_recommended_restaurants(self,recommendedModelIDs):
        query ='SELECT name, categories, stars FROM restuarants WHERE business_id IN {}'.format(list(recommendedModelIDs.values)).replace("[","(").replace("]",")")
        recommendationData = pd.read_sql(query, self.conn)
        return recommendationData
    
    def get_reviews_data(self):
        reviews_data = pd.read_sql('SELECT * FROM reviews', self.conn)
        return reviews_data

