from get_connection import db_connect

db=db_connect(password="Password@123",database="mobile")
cursor=db.cursor()
query="""
create table mobs
         (id int auto_increment primary key,
         name varchar (200) not null,
         spec varchar (200) not null,
         price int not null)"""
cursor.execute(query)