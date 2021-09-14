#finding out GCD of two Nos using NumPy Array
import timeit as tit
import numpy as np
m=int(input("write m: "))
n=int(input("write n: "))
o=int(input("write o: "))
min=min(m,n,o)
cf=np.array([])
for x in range(1,min+1):
    if m%x==0 and n%x==0 and o%x==0:
        cf=np.append(cf,x)
print(int(cf[-1]))
