class Library:
    def __init__(self, name, books: list, authors: list):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        self.books.append(book)
        author.add_book(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={self.books}, authors={self.authors})"

    def __str__(self):
        return f"Library: {self.name}\nBooks: {len(self.books)}\nAuthors: {len(self.authors)}"


class Book:
    quantity_of_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.quantity_of_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author='{self.author.name}')"

    def __str__(self):
        return f"Book: {self.name}\nYear: {self.year}\nAuthor: {self.author.name}"


class Author:
    def __init__(self, name, country, birthday, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}', books={self.books})"

    def __str__(self):
        return f"Author: {self.name}\nCountry: {self.country}\nBirthday: {self.birthday}\nBooks: {len(self.books)}"


shakespeare_books = ['Romeo and Juliet', 'Hamlet', 'Macbeth', 'Othello', "A Midsummer Night's Dream"]
christie_books = ['Murder on the Orient Express', 'And Then There Were None', 'The Murder of Roger Ackroyd',
                  'Death on the Nile', 'The ABC Murders']
author1 = Author("William Shakespeare", "England", "1564-04-23", shakespeare_books)
author2 = Author("Agatha Christie", "England", "1890-09-15", christie_books)

library = Library("My Library", author1.books + author2.books, [author1.name, author2.name])

book1 = library.new_book("Book 1", 2000, author1)
book2 = library.new_book("Book 2", 2010, author2)
book3 = library.new_book("Book 3", 2005, author1)

print(Book.quantity_of_books)
