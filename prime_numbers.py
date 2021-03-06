import math
def is_prime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n > 2 and n % 2 == 0:
		return False
	
	max_div = math.floor(math.sqrt(n))
	for d in range(3, 1 + max_div, 2):
		if n%d==0:
			return False
	return True

num = int(input())
for n in range(1,num+1):
	if is_prime(n): print(n,end=' ')		