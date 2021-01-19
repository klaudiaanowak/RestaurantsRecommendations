import sqlite3

conn = sqlite3.connect('RecommendationsDB.db')
c = conn.cursor()

c.execute("""ALTER TABLE  users ADD COLUMN haslo""")

conn.commit() 
conn.close()

conn = sqlite3.connect('RecommendationsDB.db')
c = conn.cursor()

c.execute("""ALTER TABLE  users ADD COLUMN email""")

conn.commit() 
conn.close()

conn = sqlite3.connect('RecommendationsDB.db')
c = conn.cursor()

c.execute("""ALTER TABLE  users ADD COLUMN telefon""")

conn.commit() 
conn.close()