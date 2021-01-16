import json
import numpy as np
from collections import Counter
import pandas as pd
from funcs import load_json_multiple

restuarants_type = set(["Bars","Sandwiches","Coffee & Tea","Fast Food","American (Traditional)","Pizza","Burgers","Breakfast & Brunch","Specialty Food","American (New)","Italian","Mexican","Chinese","Bakeries","Desserts","Cafes","Ice Cream & Frozen Yogurt","Japanese","Chicken Wings","Salad","Seafood","Sushi Bars","Beer","Wine & Spirits",
"Pubs","Canadian (New)","Mediterranean","Barbeque","Juice Bars & Smoothies","Steakhouses","Indian","Thai","Diners","Vietnamese","Veterinarians","Cocktail Bars","Wine Bars","Vegetarian","Ethnic Food","Greek","French","Korean","Buffets","Comfort Foo","Food Trucks","Vegan","Soup","Donuts","Hot Dogs"])

with open('dataframe_LasVegas_restaurants.json', 'r', encoding='utf-8',
                 errors='ignore') as f:
                 data=json.load(f)

data_business = []

for d in data:
    new_data_entry ={}
    new_data_entry['business_id'] = d['business_id']
    new_data_entry['name'] = d['name']
    new_data_entry['stars'] = d['stars']
    new_data_entry['review_count'] = d['review_count']
    r_type = list(set(d['categories']) & restuarants_type)
    if(len(r_type) == 0):
        new_data_entry['categories'] = None
    else:
        new_data_entry['categories'] = r_type[0]
    data_business.append(new_data_entry)

LV_dataframe = pd.DataFrame(data_business)
LV_dataframe.to_csv (r'dataframe_LasVegas_restaurants_todb.csv', index = False, header=True)
LV_dataframe.to_json (r'dataframe_LasVegas_restaurants_todb.json', orient='records')



