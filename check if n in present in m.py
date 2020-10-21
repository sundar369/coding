n=input()
m=input()
m={i:m.count(i) for i in m}
n={i:n.count(i) for i in n}
print(all([m[i]<=n.get(i,0) for i in set(m)]))