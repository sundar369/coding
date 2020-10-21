n = int(input())
narr = list(map(int,input().split()))
sarr = list(set(narr))
dic = {}
count = 0
for i in sarr:
	dic[i] = narr.count(i)
for i in dic:
	ele = dic[i]
	if ele%2==0: count+=(ele//2)
	elif ele>2: count+=((ele-1)//2)
	else: pass
print(count)