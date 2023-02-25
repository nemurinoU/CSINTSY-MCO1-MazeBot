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