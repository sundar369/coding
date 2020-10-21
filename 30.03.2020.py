import operator
d = {}
x = int(input())
listin = list(input().split())
for i in range(len(listin)):
	count = 0
	stringin = listin[i].upper()
	length = len(stringin)
	for j in range(length):
		if(stringin[j] == 'A' or stringin[j]=='E' or stringin[j]=='I' or stringin[j]=='O' or stringin[j]=='U'):
			count = count+1
	d.update({i : count})
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
fd = dict(sorted_d)
for c in fd:
	print(listin[c],end=" ")