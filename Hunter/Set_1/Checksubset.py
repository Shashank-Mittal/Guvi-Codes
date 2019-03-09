string1 = list(input().split(" "))
string2 = list(input().split(" "))
flag=0
for i in string2:
	if i not in string1:
		flag =1
if(flag==0):
	print("YES")
else:
	print("NO")