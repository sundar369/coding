n = int(input())
narr = list(map(int,input().split()))
wst,bst = narr[0],narr[0]
wc,bc = 0,0
for i in range(1,n):
	ele = narr[i]
	if ele > bst:
		bst = ele
		bc += 1
	elif ele < wst:
		wst = ele
		wc += 1
	else: pass
print(bc,wc)