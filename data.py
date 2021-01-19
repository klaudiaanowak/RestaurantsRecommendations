from tkinter import *
import sys
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('RecommendationsDB.db')
c = conn.cursor()

c.execute("""INSERT INTO  users (user_id, name, review_count, stars) VALUES('f', 'f', '0', '0')""")

conn.commit() 
conn.close()
