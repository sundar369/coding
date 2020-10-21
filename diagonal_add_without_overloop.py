x = int(input())
lst = [list(map(int,input().split())) for x in range(x)]
sum = 0
for i in range(x):
	sum = sum + lst[i][i]
if x%2==0:
	for i in range(x):
		k = x-i-1
		sum = sum+lst[i][k]
else:
	v = int(x/2)
	for i in range(x):
		if i==v:
			continue
		else:
			k = x-i-1
			sum = sum+lst[i][k]
print(sum)