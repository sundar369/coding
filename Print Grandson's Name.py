l=[];l1=[];l2=[]
for i in range(3):
    s=input().strip().split()
    l.append(s)
    l1.append(s[0])
    l2.append(s[-1])
for i in l1:
    if i not in l2:
        d=l1.index(i)
print(*l[d])