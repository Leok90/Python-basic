# autoMachineStep02_김세용
# 조건
# 사용자에게서 번호를 입력 받는다.
# 1 ~ 5 이외의 숫자 : ? "번호 확인 바람"
# 1 ~ 5
# 1번 - Orange 1000원
# ...
# 5번 - Grape 2000원
# 입력하신 구매번호는 x 입니다.
# 코인을 투입하세요: / input()
# 투입된 금액은 x 원 입니다.
# ===
# 선택한 과일 : x
# 받은금액 : x 원
# ==거스름돈==
# 거스름돈은 x원 입니다.


fruitName = ['orange', 'strawberry', 'peach', 'mango', 'grape']
fruitPrice = [1000, 2500, 1500, 2000, 2000]

print("*" * 7, "영우대학교 과일 판매 머신 V01", "*" * 7)
for i in range(len(fruitName)):
	print("[ %d. %s ] : %d 원" % (i+1, fruitName[i], fruitPrice[i]))
print("=" * 45)

while True:
	number = int(input("구매번호를 입력하세요(1~5) : "))
	if number in range(1, 6):		
		print("입력하신 구매번호는 %d 입니다.\n" % number)
		money = int(input("코인을 투입하세요 : "))
		print("투입된 금액은 %d원 입니다." % money)
		print("=" * 45)
		# 투입한 금액이 과일가격보다 큰 경우
		if money >= fruitPrice[number-1]:
			print("선택한 과일 : %d\n" % number)
			print("받은 금액 : %d원" % money)
			print("=" * 4 + "거스름돈" + "=" * 4)
			print("거스름돈은 %d원 입니다." % (money-fruitPrice[number-1]))
			break
		else: # 투입한 금액이 과일가격보다 작은 경우
			print("금액이 부족합니다.")
	else: # 잘못된 번호를 입력한 경우
		print("번호 확인 바람")