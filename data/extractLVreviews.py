
import funcs
import numpy as np
import json
from collections import Counter
import pandas as pd
import codecs



with open('dataframe_LasVegas_restaurants.json', 'r', encoding='utf-8',
                 errors='ignore') as f:
                 business = json.load(f)

restaurants_dataframe = pd.DataFrame(business)

id_business_list = list(restaurants_dataframe['business_id'])
print(len(id_business_list))

id_users_list = []
with open('dataframe_LasVegas_users.json', 'r', encoding='utf-8',
                 errors='ignore') as f:
                 users = json.load(f)

users_dataframe = pd.DataFrame(users)              
id_users_list = list(users_dataframe['user_id'])
print(len(id_users_list))


LV_reviews = []
with open('LV_reviews.json', 'r', encoding='utf-8',errors='ignore') as f:
    reviews = json.load(f)

for entry in reviews:
    if (entry['business_id'] in id_business_list and entry['user_id'] in id_users_list):
        LV_reviews.append(entry)

LV_dataframe = pd.DataFrame(LV_reviews)
LV_dataframe.to_csv (r'dataframe_LasVegas_reviews.csv', index = False, header=True)
LV_dataframe.to_json (r'dataframe_LasVegas_reviews.json', orient='records')