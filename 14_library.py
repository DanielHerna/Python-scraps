class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available  = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed!")
        else:
            print(f"{self.title} is not available")

    
    def ret(self):
        if self.available:
            print(f"{self.title} has not been borrowed")
        else:
            self.available = True
            print(f"{self.title} returned")

class User:
    def __init__(self,name, uid):
        self.name = name
        self.uid = uid
        self.borrowed_books = []

    
    def borrow_books(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{book.title} borrowed to user {self.uid}")
        else:
            print(f"{book.title} is not available")
    
    
    def ret_book(self, book):
        if book.title in self.borrowed_books:
            book.ret()
            self.borrowed_books.remove(book)
            print(f"User {self.uid} returned the book {book.title}")
        else:            
            print(f"User {self.uid} has not borrowed the book {book.title}")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Book {book.title} was added")

    def add_user(self, user):
        self.users.append(user)
        print(f"User {user.uid} was added")
    
    def show_available_books(self):
        print("Available books are: \n")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author} is available\n")
    
    def show_users(self):
        print("Available users are: \n")
        for user in self.users:
            print(f"{user.name} registered with the ID {user.uid}")


BOOK_1 = Book("The little prince", "Antoine De Saint-Exupéry")
BOOK_2 = Book("100 years of solitude", "Gabriel Garcia Marquéz")
USER_1 = User("Daniel", 123456)

LIBRARY_1 = Library()


LIBRARY_1.add_book(BOOK_1)
LIBRARY_1.add_book(BOOK_2)
LIBRARY_1.add_user(USER_1)
print("--------------------")
LIBRARY_1.show_available_books()
LIBRARY_1.show_users()
print("--------------------")
USER_1.borrow_books(BOOK_1)
LIBRARY_1.show_available_books()

USER_1.ret_book(BOOK_1)