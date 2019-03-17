try:
	number = list(map(int,input().split(" ")))
	list1 = list(map(int,input().split(" ")))
	m=list1.sort()
	k = len(list1) - number[1]
	print(list1[k])
except:
	print("Invalid Output")