from re import*
f=open("C:\\Users\\user\\Desktop\\python_codes\\email\\data.txt")
valid_emails=set()
rule="[a-zA-Z0-9][A-Za-z0-9]*[@]gmail[].]com"
for id in f:
    id=id.rstrip("\n")
    matcher=fullmatch(rule,id)
    if matcher!=None:
        valid_emails.add(id)
print(valid_emails)

