"""
Exercise 5, module 1 solution

Write a Python program that opens a PNG file in binary mode and 
prints the first 8 bytes of the file (its signature). 
Compare with https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header
"""

import os

# Gets full path of the directory where the script is
script_directory = os.path.dirname(os.path.realpath(__file__))
escaped_path = os.path.normpath(script_directory)

file = open(script_directory + "\\dice.png", "rb")
firstbytes = file.read(8)

for byte in firstbytes:
    print(hex(byte))