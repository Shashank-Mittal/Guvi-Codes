String = input()
String = String.split(" ")
temp=""
try:
	for i in range (0, len(String)):
		temp = String[i][0].upper()
		String[i] = temp + String[i][1::]
	print(" ".join(String))
except:
	print("Invalid")
