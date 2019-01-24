Inputs =[]
Number=int(input())
k="@@"
count=0
while(k!="" and count < Number):
	k=input()
	Inputs.append(k)
	count = count + 1
if(k==""):
	Inputs.pop()
prefix = []
flag = 0
i=0
while (i<len(Inputs[0])):
	count = 0
	for j in Inputs:
		if(Inputs[0][i]== j[i]):
			count = count +1
		else:
			flag=1
			break
	if(count == len(Inputs)):
		prefix.append(Inputs[0][i])
	if (flag==1):
		break
	i=i+1
if(len(prefix)>0):
	print("".join(prefix))
else:
	print("Not any Prefix Match")




