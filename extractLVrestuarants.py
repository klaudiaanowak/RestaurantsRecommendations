import json
import numpy as np
from collections import Counter
import pandas as pd
from funcs import load_json_multiple


data_business = []
with open('data_business.json', 'r', encoding='utf-8',
                 errors='ignore') as f:
   for parsed_json in load_json_multiple(f):
       data_business.append(parsed_json)

dataLV = pd.read_csv('business_dataframe_LasVegas.csv',header=0)

restaurants_data = dataLV.loc[dataLV['Restaurants'] == True] 

restaurantsIDlist = list(restaurants_data['business_id'])
print(len(restaurantsIDlist))

list_df = []
for d in data_business:
    if (d['business_id'] in restaurantsIDlist):
        list_df.append(d)

LV_dataframe = pd.DataFrame(list_df)
LV_dataframe.to_csv (r'dataframe_LasVegas_restaurants.csv', index = True, header=True)
LV_dataframe.to_json (r'dataframe_LasVegas_restaurants.json', orient='records')



