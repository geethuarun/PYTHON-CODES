from re import*
f1=open("C:\\Users\\user\\Desktop\\python_codes\\vehicles\\data.txt")
tamil=set()
kerala=set()
t_rule="[T][N][-][0-9]{2}[-][A-Z]{2}[-][0-9]{1,4}"
k_rule="[K][L][-][0-9]{2}[-][A-Z]{2}[-][0-9]{1,4}"
for w in f1:
    w=w.rstrip("\n")
    tamilrule=fullmatch(t_rule,w)
    keralarule=fullmatch(k_rule,w)

    if (tamilrule!=None):
        tamil.add(w)
    elif (keralarule!=None):
        kerala.add(w)
print(tamil)
print(kerala)