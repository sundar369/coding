x,y,z,tot = 0,0,0,0
name = ''
for i in range((int)(input().strip())):
	sname,a,b,c = input().split()
	a,b,c = int(a),int(b),int(c)
	score = a+b+c
	if tot < score:
		x,y,z,tot,name = a,b,c,score,sname
	elif tot == score:
		if a > x:
			x,y,z,tot,name = a,b,c,score,sname
		elif a==x:
			if b > y:
				x,y,z,tot,name = a,b,c,score,sname
			elif b==y:
				if c > z:
					x,y,z,tot,name = a,b,c,score,sname
				else: pass
			else: pass
		else: pass
	else: pass

print(name)