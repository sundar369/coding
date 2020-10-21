def factors(x):
    c = 0
    i = 1
    while i*i <= x:
        if x % i == 0:
            c += 1
            if x//i != i:
            	c += 1
        i += 1
    return c

num = int(input())
arr1,arr2 = [],[]
arr3,arr4 = [],[]
i = 1
while(i*i) <= num:
	if num%i==0:
		arr1.append(i)
		arr2.append(factors(i))
		if num//i != i:
			y = num//i
			arr3.append(y)
			arr4.append(factors(y))
	i += 1
arr3 = arr3[::-1]
arr4 = arr4[::-1]
print(*arr1,*arr3)
print(*arr2,*arr4)