from json import load
with open("C:\\Users\\user\\Desktop\\python_codes\\restCountries\\rest.json",encoding="UTF-8")as f:
   data=load(f)
print(len(data))
#print all country name
# for d in data:
#    print(d.get("name"))

# name=[d.get("name")for d in data ]
# print(name)

#print all region names

# regionn={d.get("region")for d in data}
# print(regionn)

# print asian countries

# asian=[d.get("name")for d in data if d.get("region")=="Asia"]
# print(asian)

#print populatn of AFG

AFG=[u.get("population")for u in data if u.get("name")=="Afghanistan" ]
print(AFG)

#india border
borders=[c.get("borders")for c in data if c.get("name")=="India"][0]
print(borders)

country_border_name=[c.get("name")for c in data if c.get("alpha3Code") in borders]
print(country_border_name)

#print currency code

code=[c.get("code")for d in data if d.get("name")=="Afghanistan" for c in d.get("currencies")]
print(code)

#highest populatn country name
maxm=max(data,key=lambda m:m.get("population"))
print(maxm.get("name"))



