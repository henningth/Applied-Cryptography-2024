"""
Exercise 10, module 1 solution

Consider the following Python code for simple random number generation.
Does this code produce consecutive random numbers? If not, suggest an improvement.
"""

import random, time
current = time.time()
random.seed(current)
r1 = random.randrange(0, 65534)
#random.seed(current) # Note we either re-seed the PRNG or not.
r2 = random.randrange(0, 65534)
print(r1)
print(r2)