#create table in database
import sqlite3
from sqlite3 import Error

def sql_connection():
   try:
       con=sqlite3.connect("D:\\ab.db")
       print("data base created successfully")

       return con
   except Error:
       print(Error)
def sql_table(con):
    curobj=con.cursor()
    curobj.execute("CREATE TABLE employees(id integer PRIMARY KEY,name text,salary real,department text,position text,hireDate text)")
    print("employee table created successfully")
    con.commit()

con=sql_connection()
sql_table(con)
       
    
