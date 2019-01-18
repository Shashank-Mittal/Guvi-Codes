Roman = list(input())
length = len(Roman)
integer =0 
flag=0
for i in range (0,length):
	if(Roman[i]=="X"):
		integer= integer + 10
		try:
			if(Roman[i-1]=="I" and (i-1)>=0):
				integer = integer -2
		except:
			pass
	elif(Roman[i]=="V"):
		integer = integer +5
		try:
			if(Roman[i-1]=="I" and (i-1)>=0):
				integer = integer -2
		except:
			pass
	elif (Roman[i]=="I"):
		integer = integer +1
	else:
		flag =1
		break
if(flag==0):
	print(integer)
else:
	print("Invalid")