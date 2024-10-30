N=362880
factor=[(x,N//x) for x in range(1,N//2 + 1) if N%x==0]
print(factor) #Technically prints out double the amount, but if the order of x and y matter then this is necessary