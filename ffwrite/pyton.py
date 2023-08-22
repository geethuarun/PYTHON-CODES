f=open("C:\\Users\\user\\Desktop\\python_codes\\ffwrite\\data.txt","w")
languages=[
    "python","java","c","c++"
]
for l in languages:
    f.write(l+"\n")

print("finished")