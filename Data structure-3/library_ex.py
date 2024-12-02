class Book:
    def __init__(self, author, title, genre, year, **kwargs):
        self.author = author
        self.title = title
        self.genre = genre
        self.year = year

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.genre}, {self.year})"

class LibraryOption1:
    def __init__(self):
        self.title_to_book = {}  # {title: Book}
        self.author_to_books = {}  # {author: [Book1, Book2, ...]}

    def add_book(self, book):
        # Add to title dictionary
        self.title_to_book[book.title] = book

        # Add to author dictionary
        if book.author not in self.author_to_books:
            self.author_to_books[book.author] = []
        self.author_to_books[book.author].append(book)

    def find_by_title(self, title):
        return self.title_to_book.get(title, "Book not found.")

    def find_by_author(self, author):
        return self.author_to_books.get(author, "No books found for this author.")

    def display_books(self):
        return list(self.title_to_book.values())
    
    
class LibraryOption2:
    def __init__(self):
        self.books_by_author = {}  # {author: {title: Book}}

    def add_book(self, book):
        # Check if the author exists in the dictionary
        if book.author not in self.books_by_author:
            self.books_by_author[book.author] = {}
        self.books_by_author[book.author][book.title] = book

    def find_by_title(self, title):
        # Search through all authors for the book by title
        for author_books in self.books_by_author.values():
            if title in author_books:
                return author_books[title]
        return "Book not found."

    def find_by_author(self, author):
        return self.books_by_author.get(author, "No books found for this author.")
    
    def display_books(self):
        #return all books
        return [
            book
            for author_books in self.books_by_author.values()
            for book in author_books.values()
        ]

# Create Book instances
book1 = Book("F. Scott Fitzgerald", "The Great Gatsby", "Fiction", 1925, isbn="123456789")
book2 = Book("George Orwell", "1984", "Dystopian", 1949)

# Option 1 Library
library1 = LibraryOption1()
library1.add_book(book1)
library1.add_book(book2)

print(library1.find_by_title("1984"))
print(library1.find_by_author("F. Scott Fitzgerald"))  

# Option 2 Library
library2 = LibraryOption2()
library2.add_book(book1)
library2.add_book(book2)

print(library2.find_by_title("1984")) 
print(library2.find_by_author("George Orwell")) 
