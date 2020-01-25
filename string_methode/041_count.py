"""count() metho returns the number of times a specified value appears in the string.
where string.count(value, start, end)
value: require. A string to value to search for
start optional. An integer, the position to start. Default is 0
end: optional. An interger, the positon to end the search. Default is the end.
"""
txt = "Hi, I am writing this text, I will have a project approach to learn python, mysql and php"
x = txt.count("python",10)
print(x)
