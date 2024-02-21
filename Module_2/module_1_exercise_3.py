"""
Exercise 3: Write a Python program which takes a text string 
as input and saves it as UTF-8 encoded variable. 
Test if it works when using Danish letters such as æ, ø, å.
"""

myString = input("Enter string:")

myStringEncoded = myString.encode("UTF-8")

print(myStringEncoded)