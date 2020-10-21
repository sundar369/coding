def splitting(exp):
	exp = list(exp)
	arr = []
	s=''
	for i in exp:
		if i.isdigit():
			s+=i
		else:
			arr.append(s)
			arr.append(i)
			s=''
	arr.append(s)
	return arr	

def evaluate(x,y,z):
	if y=='+': x+=z
	elif y=='-': x-=z
	elif y=='*': x*=z
	elif y=='/': x/=z
	else:
		x = x**z
	return x

exp = input().strip()
ar = splitting(exp)
length = len(ar)
ev = int(ar[0])

for i in range(1,length,2):
	ev = evaluate(ev,ar[i],int(ar[i+1]))
print(ev)