# import re
#how many times "a" repeat continously
# text="abababab"
# t=re.search("[a]{4}",text)
# print(t)
# text1="aaaaabbbc"
# t1=re.search("[a]{4}",text1)
# print(t1)

#repeat lowercase alpha 
# import re
# text="aaabcd123"
# t=re.search("[a-z]{4}",text)
# print(t)

import re
str="3456aaaaBCDE123"
s=re.search("[a-z]{2,3}[A-Z]{4}",str)
print(s)
