dic = {0:'0', 1:'1', 2:'8', 3:'27', 4:'64', 5:'125', 6:'216', 7:'343', 8:'512', 9:'729'}

num = list(input().strip())
out=''
for i in num:
	out += dic[int(i)]
print(out)