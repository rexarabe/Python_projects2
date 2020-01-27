#!/bin/python

"""Find is a method to find occurence of the specified value.
find() metho finds the first occurence of the specified value.
find() method return -1 if the value is not found.
find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
"""
txt = "Hello, welcome to my world."
print(txt)
x  = txt.find("e")
print(x)
