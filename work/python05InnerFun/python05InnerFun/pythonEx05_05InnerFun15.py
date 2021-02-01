# Python 내장함수 lambda
# 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할
# 함수를 한줄로 간결하게 만들 때 사용
# "람다"라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나 
# def를 사용할 수 없는 곳에 주로 사용
# 형식 : lambda 인수1, 인수2, ... : 인수를 이용한 표현식

myList = [lambda a,b:a+b, lambda a,b:a*b]

print(myList[1](3,4))