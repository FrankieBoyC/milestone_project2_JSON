import json

"""
Concerned with retrieving and storing books from a JSON file.
"""

books_file = "books.json"


def create_book_table():
    """Makes sure the JSON file exists."""
    with open(books_file, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    """Adds a book to the JSON file."""
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def get_all_books():
    """Gets all books from the JSON file."""
    try:
        with open(books_file, 'r') as file_reader:
            return json.load(file_reader)
    except IOError:
        print("Error: File not found!")


def _save_all_books(books):
    """Rewrites the JSON file."""
    try:
        with open(books_file, 'w') as file:
            json.dump(books, file)
    except IOError:
        print("Error: File not found!")


def read_book(name):
    """Iterates through the file and marks the users book as read."""
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)


def delete_book(name):
    """Removes a book from the JSON file."""
    books = get_all_books()
    books = [book for book in books if book["name"] != name]
    _save_all_books(books)





