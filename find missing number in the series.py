n = int(input())
arr = list(map(int,input().split()))
dif = int((arr[-1] - arr[0])/n)
inc = 1
ele = arr[0]
while True:
	ele += dif
	if ele != arr[inc]:
		print(ele)
		break
	inc += 1