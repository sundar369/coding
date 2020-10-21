n = input().strip()
narr = list(n)
n = int(n)
count = 0
for i in narr:
	i = int(i)
	if i == 0:
		pass
	else:
		if n%i==0: count+=1
print(count)