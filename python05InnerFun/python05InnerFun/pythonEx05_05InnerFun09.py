# Python 내장함수 filter
# 첫 번째 인수로 함수 이름을, 
# 두 번째 인수로 그 함수에 차례로 들어갈 
# 반복 가능한 자료형을 받는다.
# 두 번째 인수인 반복 가능한 자료형 요소들이 
# 첫 번째 인수인 함수에 입력되었을 때 리턴값이 참인 것만 묶어서(걸러내서) 돌려준다.

def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))