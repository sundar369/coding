a = input().strip()
b = sorted(a + input().strip())
ck = all(int(i)%2==1 for i in b)

earr,oarr = [],[]
first,mid,l1,l2 = '','','',''
zp = False
if '0' in b: zp = True

for i in b:
		if int(i)%2==1: oarr.append(i)
		else: earr.append(i)
		
if ck or len(earr)==1: print("-1")	
else:
	l1 = earr[-1]
	earr = earr[:-1]
	l2 = earr[-1]
	earr = earr[:-1]
	b = sorted(oarr + earr)
	
	if zp:
		for i in b:
			if i != '0':
				first = i
				b.remove(first)
				break
	else:
		first = b[0]
		b.remove(first)
		
	mid = ''.join(b)
	
	print(first+mid+l2+l1)			