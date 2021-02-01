# Python 내장함수 map
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력
# 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴.
def two_times(x): 
	return x*2

vMap01 = list(map(two_times, [1, 2, 3, 4]))
print(vMap01)