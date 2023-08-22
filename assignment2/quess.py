# question6

# a

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

book_title = "Book A"
book_info = library_catalog[book_title]

print(f"Title: {book_title}")
print(f"Author: {book_info['author']}")
print(f"Publication Year: {book_info['year']}")
print(f"Genre: {book_info['genre']}")


#  b


# Add a new book to the catalog
new_book_title = "Book D"
new_book_info = {
    "author": "Author D",
    "year": 2022,
    "genre": "Mystery"
}
library_catalog[new_book_title] = new_book_info

# Update the author of an existing book
existing_book_title = "Book B"
updated_author = "New Author B"
if existing_book_title in library_catalog:
    library_catalog[existing_book_title]["author"] = updated_author
    print(f"Author of '{existing_book_title}' updated to '{updated_author}'")
else:
    print(f"'{existing_book_title}' not found in the catalog")


print(library_catalog)


# c. Write a function to count how many books in the catalog were published before a given year.

def count_books_published_before_year(year):
    count = 0
    for book_info in library_catalog.values():
        if book_info["year"] < year:
            count += 1
    return count

given_year = 2005

num_books_published_before_year = count_books_published_before_year(given_year)
print(f"Number of books published before {given_year}: {num_books_published_before_year}")