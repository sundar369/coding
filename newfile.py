def is_prime(num):
	if num < 2: return False
	if num == 2: return True
	if num > 1:
	   for i in range(2,num):
	       if (num % i) == 0:
	       	return False
	   else:
	       return True
	else:
	   return False
		
def rfib(n):
   if n<=1: return n
   else: return(rfib(n-1) + rfib(n-2))

n1 = int(input())
i,ele = 0,0
farr = []


while ele<n1:
	ele = rfib(i)
	if ele <= n1:
		if is_prime(ele):
			farr.append(ele)
	i += 1

print(*farr,end=" ")