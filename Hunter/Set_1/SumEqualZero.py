try:
	number = int(input())
	string = list(map(int, input().split(" ")))
	check=0
	mini = 10000000000
	for i in range(0,len(string)-1):
		for j in range(i+1,len(string)):
			check = string[i] + string[j]
			if(check<0):
				check=-(check)
			if(check<mini):
				mini=check
				k=i
				p=j
	print(str(string[k])+" "+str(string[p]))
except:
	print("Invalid input")