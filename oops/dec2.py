def dec_square(fn):
    def inner_fn(n1,n2):
        return fn(n1**2,n2**2)
    return inner_fn

@dec_square
def add(n1,n2):
    return n1+n2  
@dec_square
def pro(n1,n2):
    return n1*n2

print(add(10,20))
print(pro(5,10))