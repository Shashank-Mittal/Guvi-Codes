try:
	length =  int(input())
	string = list(input().split(" "))
	result = []
	for i in range(0,length):
		if(i%2==0 and int(string[i])%2 !=0):
			result.append(str(string[i]))
		elif(i%2!=0 and int(string[i])%2 ==0):
			result.append(str(string[i]))
	print(" ".join(result))
except:
	print("Invalid input")