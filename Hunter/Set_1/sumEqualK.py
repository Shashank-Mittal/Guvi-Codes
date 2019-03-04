try:
	length = int(input())
	arr = list(map(int,input().split(" ")))
	result = []
	for i in range (0,len(arr)):
		for j in range(i+1,len(arr)):
			k = arr[i]+arr[j]
			for m in range (j+1,len(arr)):
				if(arr[m]==k):
					result.append([str(arr[i]),str(arr[j]),str(arr[m])])
	for i in result :
		print(" ".join(i))
except:
	print("Invalid output")

