# question6
shapes={1:"square",2:"triangle"}
num=int(input("enter a number"))
if shapes[num]=="square":
    length=int(input("length of one side"))
    print(f"Area of square={length**2}")
elif(shapes[num]=="triangle"):
    base=int(input("base of triangle"))
    height=int(input("height of triangle"))
    print(f"Area of triangle={0.5*base*height}")
else:
    print(f"No shapes available")
    

    
