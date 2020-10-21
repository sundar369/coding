import collections 

def frequency_sort(a):
    f = collections.Counter(a)
    a.sort(key = lambda x:(-f[x], x))
    return a

n = int(input())
arr = list(map(int,input().split()))
oarr = []
for i in frequency_sort(arr):
	if i not in oarr:
		oarr.append(i)
		print(i,end=" ")