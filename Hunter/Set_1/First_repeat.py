try:
	length =  int(input())
	string = list(input().split(" "))
	for i in string :
		k= string.count(i)
		if(k>1):
			k=i
			break
		else:
			k="unique"
	print(k)
except:
	print("Invalid input")