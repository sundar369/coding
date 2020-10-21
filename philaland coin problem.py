#not optimizal

no_of_ways=int(input())
for i in range(1,no_of_ways+1):
	value=int(input())
	count = 0
	while value>=1:
		value=value//2
		count=count+1
print(count)