s = list(input().strip())
if len(s)%2==1:
	print("NotAccepted")
else:
	ck = True
	oc,ec = 0,0
	for i in s:
		if ck:
			oc += int(i)
			ck = False
		else:
			ec += int(i)
			ck = True
	print(oc)
	print(ec)