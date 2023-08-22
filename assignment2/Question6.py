# Question 6

library_catalog = {
    "Book A": {
        "author": "Author A",
        "year": 2000,
        "genre": "Fiction"
    },
    "Book B": {
        "author": "Author B",
        "year": 2010,
        "genre": "Non-Fiction"
    },
    "Book C": {
        "author": "Author C",
        "year": 1995,
        "genre": "Fantasy"
    }
    
}
# add new book to catalog
library_catalog["Book D"]= {
        "author": "Author D",
        "year": 1997,
        "genre": "Fantasy"
    }
print(library_catalog)


# update author of existing book
book=library_catalog.get("Book C")
print(book)
print(book.get("author"))
book["author"]="Author u"
print(book)

# count
given_year=2000
count=0
for v in library_catalog.values():
    if v["year"]<2000:
        print(v["year"])
        count+=1
print(count)