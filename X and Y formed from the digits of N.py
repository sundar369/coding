a = list(input().strip())
b = input().strip()
c = input().strip()
ch = list(b+c)
out = "YES"
for i in ch:
	if i in a:
		a.remove(i)
	else:
		out = "NO"
		break
print(out)