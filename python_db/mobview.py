from get_connection import db_connect

class MobileView:
           def connect(self):
                   db=db_connect(password="Password@123",database="mobile")
                   return db
           
           def get(self):
                   db=self.connect()
                   cursor=db.cursor()
                   query="select * from mobs"
                   cursor.execute(query)
                   qs=cursor.fetchall()
                   return qs
           def retrieve(self,id):
                   db=self.connect()
                   cursor=db.cursor()
                   query=f"select * from mobs"
                   cursor.execute(query)
                   qs=cursor.fetchall()
                   return qs
           
mv=MobileView()
print(mv.get())