"""
maze_generator.py

This module is used to generate random maze files
that adhere to the rules of this MCO.

LIMITATIONS:

Can't add S or G...

Author(s):  Martinez, Francis Benedict V.
            
Version:    0.0.1
Date:       2023-02-22
"""
from random import randint

n = int(input ("Enter Grid Size: "))

with open (f"Test Cases/{n}x{n}.txt", "w+") as f:
    f.write (f"{n}\n")
    for i in range (n):
        for j in range (n):
            if randint (0, 10):
                f.write ('.')
            else:
                f.write ('#')
                
        f.write ('\n')