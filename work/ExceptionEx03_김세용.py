# 예외 처리
try:
	a = [1,2]
	print(a[1])
	4/0
except (ZeroDivisionError, IndexError) as e:
	print(e)