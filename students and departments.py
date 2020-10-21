dic = {}
for i in range((int)(input().strip())):
	n,d = input().split()
	dic[n] = d
dep = input().strip()

for i in dic:
	if dic[i]==dep: print(i)