# ifEx07_김세용.py
# 조건
# money와 card를 입력받는다.
# "card True 또는 False를 입력"

money = input("소지 금액을 입력하세요 : ")
card = input("card 소지 여부를 입력하세요 (True 또는 False) : ")

if int(money) >= 3000 or card == 'True' :
	print("택시를 타고 가세요.")
else:
	print("걸어 가세요.")