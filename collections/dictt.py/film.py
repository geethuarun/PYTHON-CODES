movies={"2018":5,"keralastory":3,"neymar":4,"kgf":5,"arm":4}
# for key in movies:
#     print (key,end=" ")
print(movies.keys())
print(max(movies,key=lambda w:movies.get(w)))
print(sorted(movies,reverse=True,key=lambda w:movies.get(w)))