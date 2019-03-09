try:
	number = int(input())
	string = list(map(int, input().split(" ")))
	for i in string:
		k = 0-i
		check = string.count(k)
		if(check>0):
			print(str(i)+" "+str(k))
			k="Yes"
			break
	if(k!="Yes"):
		print("There is no two element whose sum is equal or closest to zero")
except:
	print("Invalid input")