day = input().lower()
if(day=="sunday" or day == "saturday"):
	print("yes")
elif(day=="monday" or day == "tuesday" or day== "wednesday" or day=="thursday" or day=="friday"):
	print("no")
else:
	print("Invalid")