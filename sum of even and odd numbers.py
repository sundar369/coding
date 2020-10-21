n = int(input())
for _ in range(n):
	num = int(input())
	arr = list(map(int,input().split()))
	oc,ec = 0,0
	for i in arr:
		if i%2==0: ec+=i
		else: oc+=i
	print(ec)
	print(oc)