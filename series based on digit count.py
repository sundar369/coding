def rfib(n):
   if n<=1: return n
   else: return(rfib(n-1) + rfib(n-2))
       
num = int(input())
i,ele = 0,0
farr = []
odd,even = 0,0

while ele<num:
	ele = rfib(i)
	if ele <= num:
		farr.append(ele)
		if ele%2==0: even+=ele
		else: odd+=ele
	i += 1

if even >= odd:
	print(*farr,sep=" ")
else:
	n = list(str(num))
	diff = 0
	for k in n:
		k = int(k)
		if k%2!=0:
			diff += k
	st = 1
	while(st <= num):
		print(st,end=" ")
		st += diff