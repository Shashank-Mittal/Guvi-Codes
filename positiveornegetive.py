try:
	number=int(input())
	if(number>0):
		print("Positive")
	elif(number<0):
		print("Negetive")
	else:
		print("Zero")
except:
	print("Invalid Input")
