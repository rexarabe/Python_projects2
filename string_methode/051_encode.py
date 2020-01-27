#!/bin/python

"""The encode() method encodes the string, using the specidied encoding. If no encoding is specified, UTF-8 will be used."""

txt = "My name is Abdellah"

print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))
print(txt.encode(encoding="ascii", errors="strict"))
