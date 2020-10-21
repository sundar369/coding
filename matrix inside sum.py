n = int(input())
arr = []
for i in range(n): arr.append(list(map(int,input().split())))
sum = 0
for i in range(1,n-1):
	for j in range(1,n-1):
		sum += arr[i][j]
print(sum)