f=open("C:\\Users\\user\\Desktop\\python_codes\\leapyear\\data.txt","w")
years=[2000,2024,1991,1995,1200,1400,1234,2020]
for y in years:
    if(y%4==0 and y%100!=0 or y%400==0):
        f.write(str(y)+"\n")
# print("finished")


