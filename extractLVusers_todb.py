import json
import numpy as np
from collections import Counter
import pandas as pd
from funcs import load_json_multiple


with open('dataframe_LasVegas_users.json', 'r', encoding='utf-8',
                 errors='ignore') as f:
                 data=json.load(f)

data_business = []

for d in data:
    new_data_entry ={}
    new_data_entry['user_id'] = d['user_id']
    new_data_entry['name'] = d['name']
    new_data_entry['review_count'] = d['review_count']
    new_data_entry['stars'] = d['average_stars']
    data_business.append(new_data_entry)

LV_dataframe = pd.DataFrame(data_business)
LV_dataframe.to_csv (r'dataframe_LasVegas_users_todb.csv', index = False, header=True)
LV_dataframe.to_json (r'dataframe_LasVegas_users_todb.json', orient='records')



