from math import factorial

password = 13 #example of user input for how long they want there pass to be

def combos(r: int):
    n = 78 #Combined combination of characters in my password generator.
    return factorial(n) / (factorial(r) * factorial(n - r))

print("The number of password combinations is ", combos(password))