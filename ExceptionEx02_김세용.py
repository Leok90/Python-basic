# Exception_Ex02_김세용
# 예외 처리
try:
	a = [1,2]
	print(a[1])
	4/0
except ZeroDivisionError:
	print("0으로 나눌 수 없습니다.")
except IndexError:
	print("인덱싱 할 수 없습니다.")