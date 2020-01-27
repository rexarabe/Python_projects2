#!/bin/python

"""In fact, there are not many values that evaluates to False, except empty values, such
as (), [], {] "", the number 0, and the value None. And of course the value False evaluates to
False.
"""

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))
