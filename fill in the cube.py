from math import sqrt as sq
from math import floor as fl
n=int(input())
l=[]
c=0
for _ in range(n):
    l.append(list(map(str,input().split())))
for i in l:
	d_c = i.count('D')
	c += d_c
print(fl(sq(c)))