# mobiles=[
#     {"name":"galaxy","brand":"samsung","price":24000,"network":"4g","colours":["red","black","white"]}
#     ,{"name":"k7","brand":"LG","price":12000,"network":"4g","colours":["red"]}
#     ,{"name":"iphonepro7","brand":"samsung","price":80000,"network":"4g","colours":["red","white"]}]
# for m in mobiles:
#     print(m.get("price"))




clothes=[{"materials":"linen","name":"uspoloshirt","sizes":["s","m","l"],"brand":"uspolo","colors":["white","black","blue"],"price":"1500"},
{"materials":"cottonblend","name":"allensollymen casualshirt","sizes":["m","l","xl"],"brand":"allen solly","colors":["multicolour","black","blue"],"price":"1800"},
{"materials":"pure cotton","name":"louisphilippeshirt","sizes":["s","m","l"],"brand":"louisphilippe","colors":["white","maroon","blue"],"price":"1700"},
{"materials":"cottonblend","name":"peter_englandshirt","sizes":["s","xl","xxl"],"brand":"peter_england","colors":["white","black","brown"],"price":"1550"},
{"materials":"cotton blend","name":"pepe_jeansshirt","sizes":["s","m","l","xl"],"brand":"pepe_jeans","colors":["white","black","blue"],"price":"1600"}
]

for w in clothes:
    print(w.get("name"))


#nested list
name=[w.get("name")for w in clothes]
print(name)

#pepe_jeans
for c in clothes:
    if "pepe_jeans" in c.get("brand"):
        print(c.get("name"))

#costly
print(max(clothes,key=lambda c:c.get("price")))