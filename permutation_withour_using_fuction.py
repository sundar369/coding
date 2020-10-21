def permutation(lst): 
    if len(lst) == 0: 
        return [] 
    if len(lst) == 1: 
        return [lst] 
    l = []
    for i in range(len(lst)): 
       m = lst[i] 
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 

ilist = list(map(int,input().split()))
for p in permutation(ilist): 
    a = p[0] * p[1]
    b = p[2] * p[3]
    if(a==b):
    	print(a)
    	break