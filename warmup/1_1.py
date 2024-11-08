import math

def tayex_sin(X):
    """
    Coding each order of the taylor expansion, then summing it up
    """
    y=X-(X**3/math.factorial(3))+(X**5/math.factorial(5))
    return round(y,5)

x=0.1
print(f"The value of the fifth-order Taylor series expansion of sin({x}), rounded to 5 decimal places, is: {tayex_sin(x)}")

## Solution
def taylor_sin(x,n):
    result = 0
    for i in range(n+1):
        # Term in Taylor series: (-1)^i * x^(2i+1) / (2i+1)!
        term = ((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1)
        result += term
    return result

print(taylor_sin(0.1,5))