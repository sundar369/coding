#not optimizal

a = int(input())
b = int(input())

def cal(a,b):
	if a==1 or b==1:
		return 1
	else:
		return cal(a-1,b) + cal(a,b-1)
print(cal(a,b))