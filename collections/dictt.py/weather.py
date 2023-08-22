# weather=[{"tvm":25},
#          {"tvm":26},
#          {"tsr":23},
#          {"tsr":27}
#          ]
# temp={}
# for t in weather:
#     for d,w in t.items():
#         district_name=d
#         current_weather=w
#         if district_name in temp:
#             old_weather=temp[district_name]
#             if current_weather>old_weather:
#                 temp[district_name]=current_weather
#         else:
#             temp[district_name]=current_weather

# print(temp)

# print(max(temp,key=lambda w:temp.get(w)))


item = [
    {"sugar": 45},
    {"tea_powder": 28},
    {"coffee": 67},
    {"dairymilk": 170},
    {"kitkat": 70},
    {"bourborn": 50},
    {"munch": 30},
    {"milk": 80},
    {"pepsi": 99},

]

offers=[
    {"sugar":10},
    {"coffee":20},
    {"milk":5},
    {"pepsi":10}
]
wc={}
for i in item:
    for o,i in i.items():
        wc[o]=i
# print(wc)
off={}
for v in offers:
    for a,b in v.items():
        off[a]=b
# print(off)
for n,m in off.items():
    itemname=n
    vlue=m
    if itemname in wc:
        wc[itemname]-=m
print(wc)
        
        



