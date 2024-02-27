"""
Exercise 1: This exercise is about Python bytearrays.
"""
"""
(a): Begin by defining an empty bytearray, call it barr1. 
Also, define a bytes-object with contents “Python 3 programming”. Call it barr2.
"""
barr1 = bytearray()
barr2 = b'Python 3 programming'

"""
(b): Copy the contents of barr2 into barr1, except that the “3” should be a “2”. 
In other words, the resulting bytearray should read: “Python 2 programming” 
(Hint: Like lists, you can slice bytearrays: for example, 
use barr1[0:4] to get the first 4 bytes from barr1.)
"""
barr1 = barr2[0:7] + b'2' + barr2[8:]
"""
(c): Compute the number of bytes in barr1 and barr2. 
(Hint: this is like computing the number of elements in a list)
"""
print("Number of bytes in barr1:", len(barr1))
print("Number of bytes in barr2:", len(barr2))
"""
(d): What is the value and type of the fifth byte in barr1?
"""
print("Fifth byte of barr1 is", barr1[4]) # Note that it is zero-indexed. Also the letter o is 111, which is the position of this letter in the ASCII table.
print("Its type is", type(barr1[4])) # Individual byte values are integers
"""
(e): Use a Python-builtin function to find the ASCII character of the fifth byte in barr1?
"""
print(chr(barr1[4])) # Function chr() makes a lookup in the ASCII table
"""
(f): Use a Python-builtin function to print the hexadecimal representation of the bytearray barr1. 
"""
print(barr1.hex())