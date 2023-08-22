# Question1

length=3

emplst=[]

for i in range(1,length+1):
    name=input(f"Enter the {i}th name>")
    emplst.append(name)

ques=input("Want to invite anyone else to party>")
while(ques.casefold()=="yes"):
     names=input("Enter the  name>")
     emplst.append(names)
    #  print(emplst)
     ques=input("Want to invite anyone else to party>")
     if(ques.casefold()=="yes"):
        names=input("Enter the  name>")
        emplst.append(names)
        ques=input("Want to invite anyone else to party>")
        
else:
    print(f"{len(emplst)} people are invited to party")

# question2
print(emplst)
person=input("Type  in one name>")
for i in range(0,len(emplst)):
    if(emplst[i]==person):
       print(f"Position of {person} is {i}" )
       quest=input(f"Are you still want that {person} to come to party>")
       if quest.casefold()=="no":
         emplst.pop(i)
         print(emplst)
         break
       else:
        print(emplst)
    