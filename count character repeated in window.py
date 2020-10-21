def lower(low1,low2,x):
	low2 = incre
	low1 = low2-int1
	
	if low1<=0 and low2>=0: low1=0
	elif low1<0 and low2<0:
		low1,low2=0,0
	else: pass
	return low1,low2

def higher(high1,high2,x):
	if high2<length:
		high2+=1
		high1+=1
	else:
		if high1<high2: high1+=1
	return high1,high2
		
str1,int1 = input().split()
int1 = int(int1)
count,incre = 0,0
length = len(str1)
low1,low2 = 0,0
high1,high2 = 1,int1+1

while(length > incre):	
	low1,low2 = lower(low1,low2,incre)
	
	ele = str1[incre]
	chkele = str1[low1:low2]+str1[high1:high2]
	if ele in chkele: count+=1
	
	high1,high2 = higher(high1,high2,incre)	
	incre+=1
	
print(count)