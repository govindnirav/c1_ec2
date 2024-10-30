def prime_list(n):
    """
    Prints a list of prime numbers smaller than input integer, N. 
    I do not consider 1 a prime number. Using the Sieve of Erathosthenes
    """
    out=[]
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

N=100
print(prime_list(N))