f=open("C:\\Users\\user\\Desktop\\python_codes\\fileinoutput\\data.txt")
# word=[]
# for line in f:
#     text=line.rstrip("\n").split(" ")
#     for t in text:
#         word.append(t)
    
    
# print(word)

#convert to set

word=set()
for line in f:
    text=line.rstrip("\n").split(" ")
    for t in text:
        word.add(t)
    
print(word)

