# Python 내장함수 id
# 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 리턴
a = 3
b = a
vID01 = id(a)
vID02 = id(3)
vID03 = id(b)
print(vID01, " \ ", vID02, " \ ", vID03)