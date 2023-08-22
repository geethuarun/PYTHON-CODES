f=open("C:\\Users\\user\\Desktop\\python_codes\\users\\data.txt","r")
users=[]
for line in f:
    text=line.rstrip("\n")
    name,followers,following=text.split(",")
    print(name,followers,following)

