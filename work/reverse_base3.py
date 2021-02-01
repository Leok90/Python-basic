# 3진수 뒤집기
number = int(input("십진수를 입력하세요 : "))

d = []	# 나머지 리스트

while number >0:
	d.append(number%3)	# d 리스트에 나머지 값을 저장
	number = number // 3	# number를 3으로 나눈 몫으로 업데이트
d.reverse()
print("3진수 값은 : ", end="")
while d:	# d 리스트가 비어있을 때까지 반복
	print(d.pop(0), end="")
print("")