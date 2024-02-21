"""
Repeat the previous exercise but encode the 
string in ASCII instead of UTF-8. Does it work? 
Why or why not?
"""

myString = input("Enter string:")

myStringEncoded = myString.encode("ASCII")

print(myStringEncoded)