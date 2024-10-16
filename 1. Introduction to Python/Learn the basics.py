"""
# Python Basics Tutorial
# This lesson shows you the basics of the Python language. Please consider reading. I used my own name if you don't mind...

# 1. Variables and Data Types
  # In Python, you can store different types of stuff like numbers, text, and True/False values.

    # Integer (Whole number)
      a = 10
    # Float (Decimal number)
      b = 20.5
    # String (Text)
      c = "Hello, Python!"
    # Boolean (True or False)
      d = True

  # Let's print these values
    print("Integer:", a)
    print("Float:", b)
    print("String:", c)
    print("Boolean:", d)

# 2. Lists
  # A list is like a collection of items that you can change. It can hold all sorts of stuff.
    
    my_list = [1, 2, 3, "four", 5.0]
    print("List:", my_list)

# 3. Tuples
  # A tuple is like a list, but you can't change it once it's made.

    my_tuple = (10, 20, "Hello", True)
    print("Tuple:", my_tuple)

# 4. Dictionaries
  # A dictionary is a collection where each item has a key and a value, like a word and its meaning.

    my_dict = {
        "name": "Nadeem",
        "age": 16,
        "school": "CBSE"
    }
    print("Dictionary:", my_dict)

# 5. Conditional Statements
  # If you want your program to make decisions, use if, elif (else if), and else.

    x = 15
    if x < 10:
        print("x is less than 10")
    elif x == 10:
        print("x is 10")
    else:
        print("x is greater than 10")

# 6. Loops
  # Loops let you repeat stuff. You can use for loops or while loops to do something over and over.

  # For Loop (repeat a fixed number of times)
    for i in range(5):
        print("For Loop:", i)

  # While Loop (repeat while a condition is True)
    count = 0
    while count < 3:
        print("While Loop:", count)
        count += 1

# 7. Functions
  # Functions are like mini-programs inside your program. You can call them whenever you need them.

    def greet(name):
        return f"Hello, {name}!"

    print(greet("Nadeem"))

# 8. Classes and Objects
  # Python lets you create your own custom objects using classes. These are like blueprints for making things.

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def introduce(self):
            return f"My name is {self.name}, and I am {self.age} years old."
    
    person1 = Person("Nadeem", 16)
    print(person1.introduce())

# 9. Exception Handling
  # Sometimes, errors happen. Use try-except to deal with those errors without breaking your program.

    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

# 10. File Handling
  # Python can read from and write to files. It's super easy to work with files in Python.

    with open("example.txt", "w") as f:
        f.write("This is an example file.")
    
    with open("example.txt", "r") as f:
        content = f.read()
        print("File Content:", content)
"""


# I know it may seems hard in the beginning, belive me you are going to rock it
