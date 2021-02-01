# FunEx03_김세용.py
# 매개변수 지정하여 호출하기
# 1. 일반적인 함수

def add(a, b):	# a, b 는 매개변수
	return a, b, a + b

a, b, result = add(b=5, a=3)
print("%d + %d = %d " % (b, a, result))
print("-" * 20)