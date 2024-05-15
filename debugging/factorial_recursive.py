#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given integer.

    Parameters:
    - n: An integer for which factorial needs to be calculated.

    Returns:
    An integer representing the factorial of the input integer 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate the factorial of the input provided through command-line arguments
f = factorial(int(sys.argv[1]))
print(f)
