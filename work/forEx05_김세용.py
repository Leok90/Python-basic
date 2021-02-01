# forEx05_김세용
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks: # [90, 25, 67, 45, 80]
	number = number +  1  # 1 2 3 4 5
	if mark < 60:
		break	# break : 반복문을 빠져 나감
	print("%d번 학생 축하합니다. 합격입니다. " % number)