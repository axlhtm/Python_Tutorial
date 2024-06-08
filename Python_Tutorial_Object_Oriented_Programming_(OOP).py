# =============================================================================
# PYTHON TUTORIAL - OBJECT ORIENTED PROGRAMMING (OOP)
# =============================================================================

# Import Python Libraries
import datetime 
import pandas as pd 

'''
This tutorial introduces Object-Oriented Programming (OOP), a powerful paradigm for structuring your Python code. 
OOP lets you organize your code around real-world entities and their interactions.

Here are the key concepts of OOP in Python:
    * Classes: 
        Classes are blueprints that define the characteristics (attributes) and functionalities (methods) of objects.
        They act as templates for creating objects.
    * Objects: 
        Objects are instances created from a class. They hold their own specific data (attributes) 
        based on the class definition and can execute the methods defined in the class.
    * Methods: 
        Methods are functions defined within a class. They operate on the object's data (attributes) 
        and provide specific functionalities for the object.

This tutorial demonstrates these concepts through examples using `Dog` and `Book` classes. 
You'll see how to define classes, create objects (instances), and use their attributes and methods.
By the end of this tutorial, you'll have a basic understanding of OOP principles and their application in Python.
'''

# =============================================================================
# EXAMPLE I - BOOK LOAN AND RETURN SITUTATION
# =============================================================================

# Create a blank book dataframe
book_df = pd.DataFrame(columns=["Title", "Author", "Genre", "Borrower",
                                "Lend Date", "Lend Time", "Return Date", "Return Time"])

# Create an OOP Class function of for book
class book:
    ## Create a method to store information of the book
    def __init__(self, title, author, genre):
        '''
        This def function is a method that use a constructors which labelled as __init__. By using this constructors, this def 
        function is automatically called when user use class function. This function is intented to store several 
        variables that a book has, for example: book title, author, genre, etc. 
        '''
        self.title = title
        self.author = author
        self.genre = genre
        self.borrower = None
        self.lend_date = None
        self.lend_time = None
        self.return_date = None
        self.return_time = None
    ## Create a method to borrow a book
    def lend_book(self, borrower):
        if self.borrower is None:
                    self.borrower     = borrower
                    self.current_time = datetime.datetime.now()
                    self.lend_date    = self.current_time.date()
                    self.lend_time    = self.current_time.strftime("%H:%M:%S")
                    return_info = {
                        "Title": self.title,
                        "Author": self.author,
                        "Genre": self.genre,
                        "Borrower": self.borrower,
                        "Lend Date": self.lend_date,
                        "Lend Time": self.lend_time,
                        "Return Date": self.return_date,
                        "Return Time": self.return_time,
                    }
                    print(f"You borrowed {self.title} by {self.author}. Enjoy your reading!")
                    return return_info
        else:
            print(f"Sorry, {self.title} is already borrowed by {self.borrower}.")
    ## Create a method to return a book
    def return_book(self, borrower): 
        if self.borrower == borrower and self.borrower is not None:
                    self.current_time = datetime.datetime.now()
                    self.return_date = self.current_time.date()
                    self.return_time = self.current_time.strftime("%H:%M:%S")
                    return_info = {
                        "Title": self.title,
                        "Author": self.author,
                        "Genre": self.genre,
                        "Borrower": self.borrower,
                        "Lend Date": self.lend_date,
                        "Lend Time": self.lend_time,
                        "Return Date": self.return_date,
                        "Return Time": self.return_time,
                    }
                    self.borrower = None  # Reset borrower information
                    self.lend_date = None
                    self.lend_time = None
                    print(f"Thank you for returning {self.title}!")
                    return return_info
        else:
            print(f"There is no record of {borrower} borrowing {self.title}.")
            return None

# Create an OOP object instance of the Book class
book_1 = book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction")

# Simulate borrowing the book
borrowed_book_info = book_1.lend_book("Alice")
if borrowed_book_info:
    book_df = pd.DataFrame([borrowed_book_info])

# Simulate returning the book
returned_book_info = book_1.return_book("Alice")  # Return the book
if returned_book_info:
    book_df.loc[0, "Return Date"] = returned_book_info["Return Date"]
    book_df.loc[0, "Return Time"] = returned_book_info["Return Time"]