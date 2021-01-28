# Python 내장함수 list
# 반복 가능한 자료형 s를 입력받아 리스트로 만들어 리턴
# list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
vList01 = list("python")
vList02 = list((1,2,3))

a = [1, 2, 3]
b = list(a)
print(vList01, " / ", vList02, " / ", b)