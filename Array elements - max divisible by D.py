n = int(input())
narr = list(map(int,input().split()))
div = int(input())
narr.sort()
narr = narr[::-1]
for i in narr:
	if i%div==0:
		print(i)
		break