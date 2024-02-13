# Encoding and decoding
text = 'Hello world'
encoded_text = text.encode('UTF-8')
print(text)
print(encoded_text)

decoded_text = encoded_text.decode('UTF-8')
print(decoded_text)

"""
Write a Python program which takes a string as input.

This string should be encoded to UTF-8

Then, save the string in a new file.

To check if it works, write a different Python program that opens the file, decodes the data and prints the content (should be the string we got as input in the first step.)
"""

input_string = input("Enter string: ")
input_string_encoded = input_string.encode('UTF-8')

with open("myfile.txt", "wb") as file:
    file.write(input_string_encoded)

with open("myfile.txt", "rb") as file:
    content = file.read()

print(content)