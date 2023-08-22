
# question4

a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))

if (a==b==c):
    print(f"Equilateral triangle Area= {(0.43)*(a**2)},perimeter={3*a}")
elif(a==b or b==c or c==a):
    if(a==b):
       print(f"ISOSCELES triangle Area= {(0.5)*(a*c)},perimeter={(2*a)+c}")  
    elif(b==c):
       print(f"ISOSCELES triangle Area= {(0.5)*(a*c)},perimeter={(2*c)+a}") 
    else:
       print(f"ISOSCELES triangle Area= {(0.5)*(a*b)},perimeter={(2*c)+b}")
 
       
       

