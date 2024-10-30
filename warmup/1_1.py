import math


def tayex_sin(x):
    """
    Coding each order of the taylor expansion, then summing it up
    """
    y=x-(x**3/math.factorial(3))+(x**5/math.factorial(5))
    return y

print(tayex_sin(0.1))