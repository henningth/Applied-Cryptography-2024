# Live coding XOR, AND, OR

a = int('10110011', 2)
b = int('11011100', 2)

# Compute XOR:
a_xor_b = a ^ b
print(a, "XOR", b, "=", a_xor_b) # 111

# Compute OR:
a_or_b = a | b
print(a, "XOR", b, "=", a_or_b) # 255

# Compute AND:
a_and_b = a & b
print(a, "AND", b, "=", a_and_b) # 144