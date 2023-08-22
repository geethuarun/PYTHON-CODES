import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="animal"
    )
cursor=db.cursor()

query=""" 
insert into pets(age,gender,breed,location,price)values(15,'female','breed3','kozhikode',23000)
"""
cursor.execute(query)
db.commit()