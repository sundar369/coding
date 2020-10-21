#optimizal

total=int(input())
days=0
p=[]
w=[]
for i in range(0,total,+1):
    p.append(0)
    w.append(0)
for i in range(0,total,+1):
    p[i], w[i] = (map (int, input ().strip ().split (' ')))

for i in range (0, total, +1):
    days=p[i]

    while((p[i]+w[i])>6):
        w[i]+=p[i]
        p[i]=w[i]//7
        w[i]=w[i]%7
        days+=p[i]
    print(days)