#verify gmail
import re
gmail=input("enter a gmail")
g=re.search("@gmail.com$",gmail)
if g:
    print("gmail is valid")
else:
    print("gmail no valid")