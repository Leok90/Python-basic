# printExam01_김세용.py
# vList = [2, 3, 4, 5, 6, 7, 8, 9]
# 확인하고자 하는 단수 입력 : 3
# for : 반복문
# 2 * 4 = XX
# 3
# ...
# 9 * 4 = XX

vList = [2, 3, 4, 5, 6, 7, 8, 9]

num = input("확인하고자 하는 단수를 입력하세요 : ")

for i in vList:
	print(i, " * ", num, " = ", i * int(num))
