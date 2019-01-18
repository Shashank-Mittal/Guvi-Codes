String = list(input())
temp = ""
for i in range(0,len(String)-1,2):
	temp= String[i]
	String[i]=String[i+1]
	String[i+1]=temp
print("".join(String))