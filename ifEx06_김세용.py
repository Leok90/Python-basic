# ifEx06
# 조건
# money를 입력받는다.
# 3000원 이상이면 택시 가능
# 그렇지 않으면 걸어간다

money = input("소지 금액을 입력하세요 : ")

if int(money) >= 3000:
	print("택시를 타고 가세요.")
else:
	print("걸어 가세요.")