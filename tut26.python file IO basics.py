# File IO basics
#files have binary data and can be of many different types
#files can be opened in read mode
"""
"r" - Open file for reading (default mode)
"w" - for writing, we can write inside the file
"x" - exclusive creation, that means if a file doesnt exist, it creates the file
"a" - Adds more content to a file
"t" - text mode (default mode), the file is a text file e.g, notepad and reads the data as a string
"b" - binary mode,
"+" - read and write mode
"""
#Question: how to read the docstring of a function?
def func1():
    """This is"""

    print("yo")
v = (func1.__doc__)
print(v)
