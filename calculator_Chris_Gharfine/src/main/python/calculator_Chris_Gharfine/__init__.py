"""Seven basic calculator operations for Lab 6 by Chris Gharfine."""

from math import sqrt


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def modulus(x, y):
    if y == 0:
        raise ValueError("Cannot calculate modulus with a zero divisor.")
    return x % y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        raise ValueError(
            "Cannot calculate the square root of a negative number."
        )
    return sqrt(x)
