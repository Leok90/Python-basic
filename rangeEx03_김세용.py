# rangeEx03

marks = [90, 25, 67, 45, 80]
print(len(marks))		# 5 / len() : 객체의 길이
print(marks[3])	# index로 리스트 값을 가져올 수 있음
print(marks)		# 리스트 전체 값

for number in range(len(marks)):  # 0 1 2 3 4
	if marks[number] < 60:		# 1 3
		continue
	print("%d번 학생 축하합니다. 합격입니다." % (number+1))  # 0 2 4
