# from re import*

# text="luminar techno lab luminar techno hub"
# matcher=finditer("luminar",text)
# count=0
# for m in matcher:
#     print(m.start())
#     print(m.group())
#     count+=1
# print(count)


import re
text="aabbcDEFaJ3#@"
matcher=re.finditer("[a-zA-Z0-9]",text)
print(matcher)
for m in matcher:
    print(m.group())
