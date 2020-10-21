#optimizal

t =  int(input())
arr = []
arr1 = []
for i in range(0, t):
    N = int(input())
    for i in range(0, N):
        arr.append(int(input()))
    arr.sort()
    count = arr[0]
    for i in range(1, len(arr)):
        count = count + arr[i]
        arr1.append(count)
print(sum(arr1))