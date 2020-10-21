dic = {}
lnarr = []

for i in range((int)(input())):
	name = input()
	ln = name.split()[-1]
	dic[ln] = name
	lnarr.append(ln)
	
lnarr.sort()

for i in lnarr: print(dic[i])