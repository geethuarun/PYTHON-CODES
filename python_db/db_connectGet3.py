from get_connection import db_connect
db=db_connect(password="Password@123",database="animal")
cursor=db.cursor()
query="select * from pets"

cursor.execute(query)

records=cursor.fetchall()

for rec in records:
    print(rec)

