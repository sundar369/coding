n = int(input())
s = '*'
for i in range(1,n+1):
	s += str(i)
	if i%2==0: print(s[::-1])
	else: print(s)