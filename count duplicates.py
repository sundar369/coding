n = int(input())
narr = list(map(int,input().split()))

dic = {}
sarr = list(set(narr))
for i in sarr:
	dic[i] = narr.count(i)

cnt = 0
for i in dic:
	if dic[i]>1: cnt+=1

print(cnt)