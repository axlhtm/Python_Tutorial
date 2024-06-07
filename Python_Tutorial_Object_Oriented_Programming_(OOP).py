# =============================================================================
# PYTHON TUTORIAL - OBJECT ORIENTED PROGRAMMING (OOP)
# =============================================================================
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

class Dog:
  # Define attributes (characteristics) of a dog
  def __init__(self, name, breed):  # Special method called constructor
    self.name = name
    self.breed = breed

  # Define methods (behaviors) of a dog
  def bark(self):
    print(f"{self.name} says Woof!")

# Create objects (instances) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
other_dog = Dog("Luna", "Siberian Husky")

# Access object attributes and call methods
print(f"My dog's name is {my_dog.name} and breed is {my_dog.breed}")
my_dog.bark()

print(f"The other dog's name is {other_dog.name} and breed is {other_dog.breed}")
other_dog.bark()

class Book:
  def __init__(self, title, author, genre):
    self.title = title
    self.author = author
    self.genre = genre

  def lend(self, borrower):
    self.borrower = borrower
    print(f"You borrowed {self.title} by {self.author}. Enjoy your reading!")

  def return_book(self):
    self.borrower = None
    print(f"Thank you for returning {self.title}!")

# Create some Book objects
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction")
book2 = Book("Pride and Prejudice", "Jane Austen", "Romance")

# Borrow and return books
book1.lend("Alice")
book2.lend("Bob")

book1.return_book()
