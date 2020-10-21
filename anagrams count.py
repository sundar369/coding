lst1 = list(input().split())
lst2 = list(input().split())
for i in range(len(lst1)):
	lst1[i] = "".join(sorted(lst1[i]))
for i in range(len(lst2)):
	lst2[i] = "".join(sorted(lst2[i]))
count = 0
for i in lst1:
	if i in lst2: count+=1
print(count)