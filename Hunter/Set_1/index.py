length = int(input())
Numbers = input().split()
new=[]
i=0
while(i<len(Numbers)):
	if(i==int(Numbers[i])):
		new.append(str(i))
	i=i+1
if(len(new)>0):
	p = new.sort()
	print(" ".join(new))
else:
	print("-1")