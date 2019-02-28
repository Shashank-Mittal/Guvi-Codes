string = list(input().split(" "))
number = list(string[0])
K_digit = int(string[1])
Length_of_Output_number = len(number)-K_digit
minimum_number=10000000000000
for i in range(0,len(number)-Length_of_Output_number):
	mini=[]
	for j in range(i,i+Length_of_Output_number):
		mini.append(number[j])
	temporary = int("".join(mini))
	if(minimum_number>temporary):
		minimum_number=temporary
print(minimum_number)
