#optimizal

n = int(input())
lst = list(map(int,input().split()))
ans = 1
lst.sort()
for i in lst:
	if i <= ans: ans += i
	else: break
print(ans)