'''
   파일명 ] WhileEx05_오렌지.py
   조   건 ] 
	- 커피 가격이 300원이다.  판매커피수 5잔( 판매 커피 셋팅 )
		coffee = 5
	- 사용자로 부터 커피값을 입력 받는다.
	- 300원인경우 : "커피 제공 / 남은 커피 xx 잔"
	- 300원 보다 큰경우 : "커피 와 거스름돈 XX 원 / 남은 커피 xx 잔"
	- 300원 보다 작은 경우 : "커피값 확인 / 남은 커피 xx 잔"
	- 커피 개수가 0인경우 : " Sold out " 출력후 종료
	'''

idx = 5

while True:
	coffee = int(input("금액을 입력하세요 : "))
	if coffee == 300:
		idx = idx - 1
		print("커피 제공 / 남은 커피 %d 잔\n" % idx)
	elif coffee > 300:
		idx = idx - 1
		print("커피와 거스름돈 %d 원 제공 / 남은 커피 %d 잔\n" % (coffee-300, idx))
	elif coffee < 300:
		print("커피값 확인 / 남은 커피 %d 잔\n" % idx)
	
	if idx == 0 :
		print("Sold out")
		break