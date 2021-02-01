# 선택 정렬(Selection Sort)
aList = [75, 65, 100, 80, 90, 55, 95, 30, 20, 50]

for i in range(len(aList)):
	for j in range(i+1, len(aList)):
		if aList[i] > aList[j]:
			temp = aList[i]
			aList[i] = aList[j] 
			aList[j] = temp
print(aList)