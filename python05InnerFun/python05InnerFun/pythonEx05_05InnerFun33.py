# Python 내장함수 zip
# 동일한 개수로 이루어진 자료형을 묶어 주는 역할

vType01 = list(zip([1, 2, 3], [4, 5, 6]))
vType02 = list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
vType03 = list(zip("abc", "def"))

print(vType01)
print(vType02)
print(vType03)
