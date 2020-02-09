import math, random

N = 100000000
N_T = 0
for i in range(N):
    x = random.random()*2-1
    y = random.random()*2-1
    x*=x
    y*=y
    if(x+y<=1):
        N_T=N_T+1
print(4*N_T/N)