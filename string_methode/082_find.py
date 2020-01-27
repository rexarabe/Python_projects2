#!/bin/python

""" Where in the text is the first occurence of the letter '\e'\ when you only serch between
position 5 and 10?
"""

txt = "Hello, welcome to my world."

print(txt)

x = txt.find("e", 5, 10)

print(x)
