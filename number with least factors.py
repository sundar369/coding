import math 

def countDivisors(n):
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            if (n / i == i):
                cnt = cnt + 1
            else:
                cnt = cnt + 2
    return cnt

dic={}
carr = []
n = int(input())
narr = list(set(list(map(int,input().split()))))

for i in narr:
	temp = countDivisors(i)
	dic[i] = temp
	carr.append(temp)

mi = min(carr)
marr = []
for i in dic:
	a = dic[i]
	if a==mi: marr.append(i)
print(max(marr))		