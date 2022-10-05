import sqlite3
from sqlite3 import *

con = sqlite3.connect('myFile.db')
cur = con.cursor()
cur.execute("CREATE TABLE User_reg(id,email,password_1,password_2)")
res=cur.execute("SELECT email FROM User_reg")
print(res.fetchall())
