n = int(input())
diff = n//2

for i in range(diff):
	print(i+1,end=" ")
	print(n-i,end=" ")
	
if n%2==1: print(diff+1)