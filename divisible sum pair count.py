n = int(input())
div = int(input())
narr = list(map(int,input().split()))
count = 0
for i in range(n-1):
	for j in range(i,n):
		if (narr[i]+narr[j])%div == 0: count+=1
print(count)