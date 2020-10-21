#optimizal

n,cap = map(int,input().split())
l = list(map(int,input().split()))
m = []
lit = 0
for i in range(len(l)):
	lit += l[i]
	k = lit//cap
	lit -= (k*cap)
	k = k%10
	m.append(str(k))
print("".join(m))