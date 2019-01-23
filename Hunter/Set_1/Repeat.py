string = input()
Numbers = string.split(" ")
Set = set(Numbers)
new=[]
for i in Set:
	count = string.count(i)
	if(count>1):
		new.append(i)
m= new.sort()
if(len(new)>0):
	print(" ".join(new))
else:
	print("unique")
