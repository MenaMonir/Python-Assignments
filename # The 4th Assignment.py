#                                                           Name  : -     Mena Monir Helal
#                                                           Course: -       Python & AI
#                                                                        The 4th Assignment

# Task: Library Management System
# Create a simple Library Management System that include classes for Library, Book, and Member

print("This is a program that represents a simple library management ")


#  ---/ 1. Classes and Objects /---
    # Create a Book class with:
    # Attributes: title, author, isbn, and available (default True).
    # Methods:
    #   __init__: To initialize the attributes.
    #   display_info: To print the book's title, author, ISBN, and availability.

class Book:    
    def __init__(self, title, author, isbn):                        # Represents a book in the library.
        self.title = title
        self.author = author
        # Encapsulation: Using a private attribute for ISBN
        self.__isbn = isbn
        self.available = True

    def display_info(self):                                        # Prints the book's details, including availability.
        
        status = "Available" if self.available else "Borrowed"
        print(f"--- Book Details ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.get_isbn()}")
        print(f"Status: {status}")

    # Getter for the private ISBN attribute
    def get_isbn(self):
        return self.__isbn

    # Setter for the private ISBN attribute (optional, but good practice for encapsulation)
    def set_isbn(self, new_isbn):
        if isinstance(new_isbn, str) and new_isbn:
            self.__isbn = new_isbn
            print(f"ISBN updated for '{self.title}'.")
        else:
            print("Invalid ISBN provided.")

class Member:                                                      # Represents a library member.
   
    def __init__(self, name, membership_id):
        self.name = name
        # Encapsulation: Using a private attribute for membership_id
        self.__membership_id = membership_id
        self.borrowed_books = []

    def get_membership_id(self):
        return self.__membership_id

    def borrow_book(self, book):                                   # Allows the member to borrow a book if it is available.
        
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed '{book.title}'.")
            return True
        else:
            print(f"'{book.title}' is currently unavailable.")
            return False

    def return_book(self, book):                                   # Allows the member to return a borrowed book.
        
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} successfully returned '{book.title}'.")
            return True
        else:
            print(f"{self.name} did not borrow '{book.title}'. Cannot return.")
            return False

class StaffMember(Member):                                         # Represents a staff member, inheriting from the Member class.
    
    def __init__(self, name, membership_id, staff_id):             # Staff members have additional privileges, like adding books.
        # Call the parent class (Member) constructor
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, title, author, isbn):              # Allows a staff member to create and add a new book to the library's collection.
       
        new_book = Book(title, author, isbn)
        library.add_book(new_book)
        print(f"Staff member {self.name} (ID: {self.staff_id}) added '{new_book.title}' to the library.")
        return new_book

class Library:                                                     # Manages the collection of books and members.
    
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library collection.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered.")

    def list_books(self):
        print("\n--- Current Library Collection ---")
        if not self.books:
            print("The library is currently empty.")
            return
        for book in self.books:
            book.display_info()
            print("-" * 20)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# --- Demonstration ---

print("--- Library Management System Demo ---")

# 1. Initialize the library
main_library = Library()

# 2. Initialize members
print("\n--- Initializing Members ---")
member1 = Member("Alice Johnson", "M001")
staff1 = StaffMember("Bob Smith", "M002", "S001")

main_library.register_member(member1)
main_library.register_member(staff1)

# 3. Staff member adds books (using the inherited and new methods)
print("\n--- Staff Adding Books ---")
book1 = staff1.add_book(main_library, "The Python Handbook", "J. Doe", "978-0123456789")
book2 = staff1.add_book(main_library, "Data Structures in Python", "A. Coder", "978-9876543210")

# 4. Display current library collection
main_library.list_books()

# 5. Encapsulation check (accessing private attributes via getters)
print("\n--- Encapsulation and Access ---")
print(f"Book 1 ISBN (via getter): {book1.get_isbn()}")
print(f"Member 1 ID (via getter): {member1.get_membership_id()}")

# 6. Member borrowing and returning a book
print("\n--- Borrowing and Returning ---")
member1.borrow_book(book1)

# Check the availability status after borrowing
book1.display_info()

# Attempt to borrow the same book (should fail)
member1.borrow_book(book1)

# Member returns the book
member1.return_book(book1)

# Check the availability status after returning
book1.display_info()

# 7. List books again to confirm availability change
main_library.list_books()
