def rd(s):
	n = len(s)
	if n<2:
		return
	j = 0
	for i in range(n):
		if s[j]!=s[i]:
			j += 1
			s[j] = s[i]
	j += 1
	s = s[:j]
	return s

st = input().strip()
st = list(st.rstrip())
st = rd(st)
print(*st,sep="")