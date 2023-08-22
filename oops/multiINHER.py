class P1:
    def m1(self):
        print("class p1 m1 method")

class P2:
    def m2(self):
        print("p2 m2 method")

class C(P1,P2):
    pass
obj=C()
obj.m1()#in c thereis no method 1 so it take from 1st class p1