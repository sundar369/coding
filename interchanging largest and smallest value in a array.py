n = int(input())
narr = list(map(int,input().split()))
mi = narr.index(min(narr))
ma = narr.index(max(narr))
narr[mi] , narr[ma] = narr[ma] , narr[mi]
print(*narr)