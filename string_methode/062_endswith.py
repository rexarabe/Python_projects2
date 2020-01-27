#!/bin/python

"""Check if position 5 to 11 ends with the phrase my world.

"""

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)
