#insert record into table of database
import sqlite3
con=sqlite3.connect("D:\\ab.bd")
def sql_insert(con,entities):
    curobj=con.cursor()
    curobj.execute("INSERT INTO employees(id,name,salary,department,position,hireDate)VALUES(?,?,?,?,?,?)",entities)
    print("1 row inserted")
    con.commit()
entities=(1,"karthikeya",100000000000,"cse","Tech","1/9/2023")
sql_insert(con,entities)
