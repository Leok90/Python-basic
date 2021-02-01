# 3진수 뒤집기
number = input("십진수를 입력하세요 : ")

n = []	# 몫
d = []
i = 0
x = 0
while number >3:
	n.append(number//3)
	d.append(number%3)
	number = number // 3
print(n, d)