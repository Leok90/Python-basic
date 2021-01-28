# Python 내장함수 map
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력
# 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴.
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)