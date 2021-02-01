# Python 내장함수 map
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력
# 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴.
#  lambda를 사용하면 다음처럼 간략하게 만들 수 있다.

vMap01 = list(map(lambda a: a*2, [1, 2, 3, 4]))
print(vMap01)