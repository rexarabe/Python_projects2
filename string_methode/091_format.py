#!/bin/python

"""
The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.
"""

txt1 = "My name is {fname}, I'am{age}".format(fname = "John", age = 36)
print(txt1)
txt2 = "My name is {0}, I'am {1}".format("John", 36)
print(txt2)
txt3 = "My name is {}, I'am {}".format("John", 36)
print(txt3)
