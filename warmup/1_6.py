N=362880
factor=[(x,N//x) for x in range(1,int(N**0.5) + 1) if N%x==0] ##Using the sqrt to avoid mirroring pairs
print(factor)