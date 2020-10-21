sarr = []
for i in range(97,97+26):
	x = str(chr(i))
	sarr.append(x)
st = list(input().strip().split())
s = ''
for i in st:
	s += i
st = sorted(list(set(list(s.lower()))))
if sarr == st: print("yes")
else: print("no")