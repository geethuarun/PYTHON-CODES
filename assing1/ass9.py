# question9

num=int(input("no of people invite for party"))
if num<10:
    for i in  range(1,num+1):
        name=input("enter a name")
        print(f"{name} has been invited")
elif(num>10):
    print("Too many people")
