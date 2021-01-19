import sqlite3 as sql
import pandas as pd

business = pd.read_csv('dataframe_LasVegas_restaurants_todb.csv', index_col='business_id')
users = pd.read_csv('dataframe_LasVegas_users_todb.csv', index_col='user_id')
reviews = pd.read_csv('dataframe_LasVegas_reviews.csv', index_col='review_id')

conn = sql.connect('RecommendationsDB.db')
c = conn.cursor()


try:
    business.to_sql('restuarants', conn, index=True, index_label='business_id')
except:
  print("Table \"restaurants\" already exists")

try:
    users.to_sql('users', conn, index=True, index_label='user_id')
except:
  print("Table \"users\" already exists")

try:
    reviews.to_sql('reviews', conn, index=True, index_label='review_id')
except:
  print("Table \"reviews\" already exists")

c.execute('ALTER TABLE restuarants ADD model_id INTEGER')
c.execute('ALTER TABLE users ADD model_id INTEGER')
c.execute("ALTER TABLE  users ADD COLUMN haslo")
c.execute("ALTER TABLE  users ADD COLUMN email")
c.execute("ALTER TABLE  users ADD COLUMN telefon")

for user in users.index:
    query = "UPDATE users SET haslo = '{}' WHERE user_id='{}'".format("pass"+user, user)
    c.execute(query)



c.execute("INSERT INTO users (user_id, name, haslo) values(?,?,?)",('admin','Administrator','admin'))
conn.commit()


restaurants_data = pd.read_sql('SELECT * FROM restuarants', conn)
users_data = pd.read_sql('SELECT * FROM users', conn)
reviews_data = pd.read_sql('SELECT * FROM reviews', conn)

print(restaurants_data)
print(users_data)
print(reviews_data)