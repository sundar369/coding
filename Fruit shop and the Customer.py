n = int(input())
arr = list(input().split())
a,o = map(int,input().split())

for i in arr:
	if i[0]=='A': a+=int(i[1:])
	else: o+=int(i[1:])

for i in arr:
	if i[0]=='A':
		a-=int(i[1:])
		if a==o: print(a,o)
	else:
		o-=int(i[1:])
		if a==o: print(a,o)