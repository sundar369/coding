row,col = map(int,input().split())
arr = []
for i in range(row): arr.append(list(map(int,input().split())))
n,m = map(int,input().split())
chg = m*n
bchg = m*n*2

for i in range(row):
	for j in range(col):
		if i==0 or j==0 or i==row-1 or j==col-1: print(arr[i][j]+bchg,end=" ")
		else: print(arr[i][j]+chg,end=" ")
	print()