fread=open("C:\\Users\\user\\Desktop\\python_codes\\num\\data.txtt","r")
fwrite=open("C:\\Users\\user\\Desktop\\python_codes\\num\\data.txt","w")
for line in fread:
    year=int(line.rstrip("\n"))
    if (year%4==0 and year%100!=0 or year%4==0):
        fwrite.write(str(year)+"\n")
print("finished")