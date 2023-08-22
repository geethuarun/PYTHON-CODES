# question5
ques1=input("if it is raining")
if (ques1.casefold()=="yes"):
    ques2=input("if it is windy")
    if(ques2.casefold()=="yes"):
        print("it is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")