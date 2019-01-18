try:
	Number = int(input())
	CNumber=Number
	count=0
	while(CNumber!=0):
		CNumber=CNumber//10
		count = count +1
	count = count -1
	Reversed_number=0
	while (Number >0):
		Reversed_number = ((Number % 10) * (10**count)) + Reversed_number
		count=count-1
		Number = Number//10
	print(Reversed_number)
except:
	print("Invalid")