# Python 내장함수 int
# 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 리턴
# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환
vInt01 = int('3')
vInt02 = int(3.6)
vInt03 = int('10', 2)
vInt04 = int('20', 8)
vInt05 = int('10', 16)
print(vInt01, " \ ", vInt02, " \ ", vInt03, " \ ", vInt04, " \ ", vInt05)