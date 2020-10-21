n = int(input())
arr = []
for _ in range(n):
	arr.append(input().strip())
arr = sorted(arr)
for i in arr[::-1]: print(i)