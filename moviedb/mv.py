from json import load
with open("C:\\Users\\user\\Desktop\\python_codes\\moviedb\\mdb.json","r",encoding="UTF-8") as f:
   data=load(f)
#total no of movies
print(len(data))
#print all movie names
# movie_names=[m.get("title")for m in data]
# print(movie_names)
# #print movie with highest run time
# lengthy=max(data,key=lambda m:int(m.get("runtime")))
# print(lengthy.get("title"))

#print all genres
# genres_name={g for m in data  for g in m.get("genres")}
# print(genres_name)


#print movie name which contain genres comedy
# for m in data:
#    if "Comedy" in m.get("genres"):
#         print(m.get("title"))
comedy_genre=[m.get("title")for m in data if "Comedy" in m.get("genres")]
print(comedy_genre)

# print movie name which contain  genres comedy or Fanstasy
comedy_genre={m.get("title")for m in data  for g in m.get("genres")if g in  ["Comedy","Fantasy"]  }
print(comedy_genre)

#yearwise movie count {1988:5,1984:3}
# wc={}
# for m in data:
#     if m.get("year") in wc:
#        wc[m.get("year")]+=1
#     else:
#        wc[m.get("year")]=1
# print(wc)
# print(max(wc,key=lambda k:wc.get(k)))
# print(min(wc,key=lambda k:wc.get(k)))

lengthy=max(data,key=lambda m:int(m.get("runtime")))
print(lengthy.get("title"))
