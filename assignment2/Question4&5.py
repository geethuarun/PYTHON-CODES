# question4


emplst=[]
length=4
for i in range(0,4):
    id=int(input("Enter an id>"))
    name=input("Enter a name>")
    age=int(input("Enter the age>"))
    wc={"name":name,"id":id,"age":age}
    emplst.append(wc)
    print(emplst)

name=input("Enter a name>")
for i in emplst:
    if i["name"]==name:
        print(f"AGE:{i['age']},ID:{i['id']}")
#question5
for u in emplst:
    u.pop("id")
    print(u)
print(emplst)
