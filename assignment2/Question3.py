# question3

lst=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in lst:
    row=int(input("Enter the row number>"))
    print(lst[row])
    break
value=int(input("Enter a value>"))
lst[row].append(value)
print(lst[row])