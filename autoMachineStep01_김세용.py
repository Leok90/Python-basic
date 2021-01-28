# autoMachineStep01_김세용
# 조건
# 사용자에게서 번호를 입력 받는다.
# 1 ~ 5 이외의 숫자 : ? "번호 확인 바람"
# 1 ~ 5
# 1번 - Orange 1000원
# ...
# 5번 - Grape 2000원


fruitName = ['orange', 'strawberry', 'peach', 'mango', 'grape']
fruitPrice = [1000, 2500, 1500, 2000, 2000]

print("*" * 7, "영우대학교 과일 판매 머신 V01", "*" * 7)
for i in range(len(fruitName)):
	print("[ %d. %s ] : %d 원" % (i+1, fruitName[i], fruitPrice[i]))
print("=" * 45)

while True:
	number = int(input("구매번호를 입력하세요(1~5) : "))
	if number in range(1, 6):		
		print("%d번 %s %d원" % (number, fruitName[number-1], fruitPrice[number-1]))
	else:
		print("번호 확인 바람")