#optimizal

n = int(input())
five = int((n-4)/5)
if ((n-5*five)%2)==0: one=2
else: one=1
two = (n-5*five-one)//2
print(five+two+one,five,two,one)