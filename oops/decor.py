def dec_fun(fn):#fn=sub(10,20)
    def inner_fun(n1,n2):#inner_fun(10,20)
        if n1<n2:
            (n1,n2)=(n2,n1)#n1=20 n2=10
        return fn(n1,n2) #sub(20,10)
    return inner_fun 
@dec_fun
def sub(n1,n2):
    return n1-n2  
@dec_fun
def div(n1,n2):
    return n1/n2

print(sub(10,20))
print(div(5,10))