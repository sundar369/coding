n = int(input())
narr = list(map(int,input().split()))
ev,od = 0,0
for i in range(n):
	if narr[i]%2==0: ev+=narr[i]
	else: od+=narr[i]
print(od-ev)