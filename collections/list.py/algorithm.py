lst=[10,10,20,20,30,40,40,60]
p1=0
p2=1
print(len(lst))
while p1<len(lst) and p2<len(lst):
    if (lst[p1]-lst[p2]==0):
        lst.pop(p1)
        p1+=1
        p2+=1
    else:
        p1+=1
        p2+=1
print(lst)