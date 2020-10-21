n = int(input())
for _ in range(n):
	num = int(input())
	ud = num % 10
	if num <= 37: print(num)
	elif ud < 3: print(num)
	elif ud < 6: print(str(num)[:-1]+'5')
	elif ud < 8: print(num)
	elif ud == 8: print(num+2)
	else: print(num+1)