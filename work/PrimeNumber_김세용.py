 # 파일명 ] PrimeNumber_오렌지.py
#   조   건 ] 
#	- >> 20이상의 수를 입력하세요 :
#	- 이하인경우 : ? 숫자 확인하세요.
#	- 이상인경우 : 소수 판별 출력
#	-----------------------------
#   Sample Run ] 
#	1 소수 X
#	2 소수 O.
#	3 소수 O.

#	...

#	16 소수 X.
#	17 소수 O.
#	18 소수 X.
# 나누어 떨어지는 횟수가 2회 일 경우 = 소수

num = int(input("20이상의 수를 입력하세요 : "))

if(num<20):
	print("숫자 확인하세요.")
else:
	for i in range(1, num+1):
		count1 = 0
		for j in range(1, i+1):
			if i % j == 0:
				count1 = count1 + 1
		if count1 == 2:
			print("%d는 소수 O" % i)
		else:
			print("%d는 소수 X" % i)

