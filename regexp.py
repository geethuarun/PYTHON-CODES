sen="joel is a very good studentin may batch"
# bol=sen.startswith("joel")
# print(bol)
# if bol==True:
#     print("The sentence is staring with joel")

#Without using startswith
# word=sen.split()
# if word[0]=="joel":
#     print("The sentence is staring with joel")

#for checking 1st word is joel
# import re
# sen="joel is a very good studentin may batch"
# x=re.search("^joel",sen)
# print(x)
# y=re.search("^is",sen)
# print(y)
# import re
# sen="is a very good studentin may batch joel"
# # end=re.search("joel$",sen)
# # print(end)
# st_en=re.search("^is.*joel$",sen)
# print(st_en)
# 
#in case of space at last
import re
sen="joel is a very good studentin may batch"
# arch("^joel.*batst_en1=re.sech",sen)
# print(st_en1)
sen="joel is a very good studentin may batch   "
st_en2=re.search("^joel.*batch$",sen)
print(st_en2)
