#!/bin/python

"""If the value is not found, the find() method returns -1, but the index() method will raise and exception"""

txt = "Hello, welcome to my world."

print(txt)

print(txt.find("q"))
print(txt.index("q"))
