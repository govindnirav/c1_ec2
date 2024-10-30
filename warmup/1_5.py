import math

N=100

def prime_list(n):
    """
    Returns a list of the first N prime numbers. 
    I do not consider 1 a prime number. Using the Sieve of Erathosthenes:
    Essentially creates a list of length n+1 (n+1 for indexing purposes)
    For each value, p, in sieve, it checks if p==TRUE. If so, it appends p to out.
    It also turns every multiple of p in sieve into false. (A multiple can't be a prime number)
    """
    if n < 6:  # Avoids log(0) issues
        ub = 15
    else:
        ub = int(n * math.log(n) + n * math.log(math.log(n)))
    out=[]
    sieve = [True] * (ub+1)
    for p in range(2,ub+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, ub+1, p):
                sieve[i] = False
    return out

def recaman_sq(n):
    out=[]
    x=0
    for i in range (0, n):
        if x==0 and x not in out:
            out.append(x)
        elif (x-i)>0 and x-i not in out:
            x = x-i
            out.append(x)
        else:
            x = x+i
            out.append(x)
    return out

pr=prime_list(N)
rs=recaman_sq(N)

def compare(ls1, ls2):
    out=[]
    for i in ls1:
        if i in ls2 and i not in out:
            out.append(i)
    return out

print(compare(pr,rs))
        
