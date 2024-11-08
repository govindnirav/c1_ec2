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

## Correction

def random_walk():
    position = 0
    while abs(position) < 10:
        position += 1 if random.randint(0, 1) else -1
        yield position # Yield is different from return. Remembers thing only 1 then 'deletes'

for p in random_walk():
    print(p, end = " ")

"""
Gambler's ruin.
Fact that a gambler playing a game with negative expecter return will eventually go bankrupt.
"""
    