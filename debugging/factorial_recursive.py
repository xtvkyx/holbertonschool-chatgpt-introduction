#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function: Calculate the factorial of a number recursively.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number n. 
         Returns 1 if n is 0 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from command line arguments, calculate factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)
