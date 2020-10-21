narr = list(map(int,input().split()))[::-1]
oarr = []
ele = narr[0]
oarr.append(ele)
for i in narr:
	if ele < i:
		oarr.append(i)
		ele = i
print(*oarr[::-1])