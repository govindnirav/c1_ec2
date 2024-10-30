import random

def rand_walk(n):
    """
    Prints it out in the form of a list
    """
    out=[]
    i=0
    while abs(i) in range(n):
        x = random.randint(0,1)
        if x == 1:
            i+=1
            out.append(i)
        else:
            i-=1
            out.append(i)
    return out

print(rand_walk(10))

    