lst=[1,2,3,4,5]

#to find square
# def square(num):
#     return num**2


# square=list(map(lambda num:num**2,lst))
# print(square)


# cube=list(map(lambda num:num**3,lst))
# print(cube)

#filer()

# def odd_num(n):
#     return n%2!=0

# odds=list(filter(odd_num,lst))
# print(odds)

# odds=list(filter(lambda n:n%2!=0,lst))
# print(odds)




# evenss=list(filter(lambda n:n%2==0,lst))
# print(evenss)

# gt=list(filter(lambda n:n>3,lst))
# print(gt)

items=[
    {"name":"biriyani","price":130,"category":"nonveg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vegfriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"},
    
]


#print all items name

# items_name=list(map(lambda it:it.get("name"),items))
# print(items_name)



#list comprehension
# items_name=[it.get("name") for it in items]
# print(items_name)

price=list(map(lambda it:it.get("price"),items))
print(price)

lst_price=[it.get("price")for it in items]
print(lst_price)

veg=list(filter(lambda it:it.get("category")=="veg",items))
print(veg)
# for getting name of veg
for v in veg:
    print(v.get("name"))