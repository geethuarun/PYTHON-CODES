from json import load
with open("C:\\Users\\user\\Desktop\\python_codes\\jsonprocess\\data.json","r") as f:
    data=load(f)

names=[u.get("name") for u in data]
print(names)
#student with highest mark
print(max(data,key=lambda u:u.get("total")))
#sort by student wrt total
print(sorted(data,reverse=True,key=lambda s:s.get("total")))
#print bca students
bca_students=[u.get("name")for u in data if u.get("course")=="bca"]
print(bca_students)