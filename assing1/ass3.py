
# question3
from re import*
password=input("Enter your password")
rule="[a-z]{1}[A-Z]{1}[0-9]{1}[^a-z A-Z 0-9]{1}[a-z A-Z 0-9]{6,16}"
match=fullmatch(rule,password)
if match!=None:
    print("Password valid")
else:
    print("Password notvalid")
