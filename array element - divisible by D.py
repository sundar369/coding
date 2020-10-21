n = int(input())
narr = list(map(int,input().split()))
d = int(input())
for i in narr:
	if i%d==0: print(i,end=" ")