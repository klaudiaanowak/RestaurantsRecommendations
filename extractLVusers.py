import json
import operator
import numpy as np
from collections import Counter
import pandas as pd

user_data = []
with open('activ_users_data_LV.json', 'r', encoding='utf-8',
                 errors='ignore') as f:
                 user_data = json.load(f)

user_dataframe = pd.DataFrame(user_data)

del user_dataframe['friends']
user_dataframe.to_csv (r'dataframe_LasVegas_users.csv', index = True, header=True)
user_dataframe.to_json (r'dataframe_LasVegas_users.json', orient='records')


