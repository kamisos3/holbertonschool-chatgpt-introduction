#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <non-negative integer>".format(sys.argv[0]))
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        print(factorial(num))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
