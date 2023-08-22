year=int(input("enter a number"))
is_leapyear=False
if (year%4==0 and year%100!=0 or year%400==0):
    is_leapyear=True
    print (year, is_leapyear)
else:
    print(year,is_leapyear)