#optimizal

tc = int(input())
for _ in range(tc):
	a,b,c = map(int,input().split())
	minx = (a-c)+1
	if b==0:
		print(c)
	elif b==minx or (a==b and c==1):
		print(a)
	elif b<minx:
		print(c+b-1)
	else:
		b -= minx
		if b > a:
			while(b > a):
				b -= a
			print(b)
		else:
			print(b)