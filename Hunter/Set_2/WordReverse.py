string = list(input().split(" "))
new=[]
for i in string:
	k=list(i)
	m=k.reverse()
	list1="".join(k)
	new.append(list1)
print(" ".join(new))