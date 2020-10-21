mod = 10**9+7
from itertools import product
l,h=map(int,input().split())
constant=int(input().strip())
lst=[]
c = 0
for i in range(l,h+1):
    lst.append(str(i))
all_poss=product(lst,repeat=constant)
for i in all_poss:
    number = 0
    for x in i: number += int(x)
    if number%2==0: c+=1
print(c%mod)