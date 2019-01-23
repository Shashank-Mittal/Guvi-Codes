size = int(input())
Numbers = input().split(" ")
Set = set(Numbers)
for i in Numbers:
	if(Numbers.count(i)<2):
		print(i)
		break