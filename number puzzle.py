#optimizal

def puzz(n,lst):
	input2.sort()
	s=0
	for i in range(n-1,0,-1):
		s += abs((input2[i])-(input2[i-1]))
	print(s)

n = int(input())
lst = list(map(int,input().split()))
puzz(n,lst)