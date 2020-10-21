from math import gcd as gcd
t=int(input())
for k in range (t):
	n=int(input())
	a=list(map(int, input().split()))
	i, ans, c=0,1,0
	while(i<=n-1):
		temp_i=i
		c=0
		while(a[i]!=0):
			temp=i
			i=a[i]-1
			a[temp]=0
			c+=1
		i=temp_i+1
		if c!=0:
			ans = ans*c//gcd(ans,c)
	print(ans)