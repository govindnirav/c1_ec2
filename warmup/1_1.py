import math

def tayex_sin(X):
    """
    Coding each order of the taylor expansion, then summing it up
    """
    y=X-(X**3/math.factorial(3))+(X**5/math.factorial(5))
    return round(y,5)


x=0.1
print(f"The value of the fifth-order Taylor series expansion of sin({x}), rounded to 5 decimal places, is: {tayex_sin(x)}")
