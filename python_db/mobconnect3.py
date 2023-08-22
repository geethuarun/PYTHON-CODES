from get_connection import db_connect

db=db_connect(password="Password@123",database="mobile")
cursor=db.cursor()
query="""
insert into mobs(name,spec,price)values
        ('samsung galaxy s21 FE 5G','6.4 inch Dynamic AMOLED 2X',50000),
        ('One plus Nord CE Lite 4G','6.59 inch',55000),
        ('vivo Y100 5G','6.38 inch Full HD+Amoled display',30000)
"""
cursor.execute(query)
db.commit()