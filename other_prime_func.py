#!/usr/bin/python3

"""
Very fast prime number determiner... 

https://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
    
"""
def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i**2 <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
        
