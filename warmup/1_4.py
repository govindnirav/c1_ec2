
def recaman_sq(n):
    """
    Redefining the recaman sequence funtion using python.
    """
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

n=100
print(recaman_sq(n))