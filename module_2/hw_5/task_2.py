class Library:
    def __init__(self, name, books: list, authors: list):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author):
        pass

    def __repr__(self):
        return f"Library({self.name})"

    def __str__(self):
        return f"{self.name} Library"


class Book:
    quantity_of_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return f"{self.name} by {self.author.name}, {self.year}"


class Author:
    def __init__(self, name, country, birthday, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return f"{self.name} ({self.country}), born on {self.birthday}"
