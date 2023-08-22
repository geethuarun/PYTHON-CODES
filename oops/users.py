class Users:
    data=[
        {"id":1,"username":"jhon","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
    ]
    def get(self):
        return self.data
    def retrieve(self,id):
        return[u for u in self.data if u.get("id")==id]


    def post(self,obj):
        self.data.append(obj)

    def destroy(self,id):
        o=[u for u in self.data if u.get("id")==id][0]
        self.data.remove(o)
    def put(self,id,value):
        ob=[u for u in self.data if u.get("id")==id][0]
        # print(value)
        pos=self.data.index(ob)   
        self.data[pos]=value[0]

obj=Users()
# print(obj.getall_users())
# print(obj.()
# stu={"id":7,"username":"gowri","email":"gowri@gmail","password":"password123"}
# obj.post(stu)
# print(obj.get())
# obj.destroy(5)
# print(obj.get())

data={"id":6,"username":"toms","email":"toms@gmail.com","password":"password@123"}
print(obj.put(6,data))







# class Film:
#     movies=[
#     {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
#     {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
#     {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
#     {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
#     {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
#     {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
#     {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
#     {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
#     {"language":"telungu","name":"kgf","rating":15,"year":2018,"genres":["action","romance","thriller"]}

# ]

#     def get(self):
#         return self.movies
    
#     def retrieve(self,name):
#         return [m for m in self.movies if m.get("name")==name]
    
#     def post(self,value):
#         return self.movies.append(value)
#     def destroy(self,name):
#         o=[m for m in self.movies if m.get("name")==name][0]
#         self.movies.remove(o)

    
    
# ob=Film()
# # print(ob.get())
# # ob.retrieve("kgf")
# value={"language":"malayalam","name":"one","rating":5,"year":2023,"genres":["mystery"]}
# ob.post(value)
# print(ob.get())
# ob.destroy("kgf")
# print(ob.get())




    

    
