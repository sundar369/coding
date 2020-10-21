n = int(input())
for _ in range(n):
	a,b = map(float,input().split())
	print("{:.2f}".format(a*b))