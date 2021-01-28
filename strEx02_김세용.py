# strEx02_김세용.py

# 문자열 슬라이싱이란?

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
'''
 인덱싱 기법과 슬라이싱 기법은 뒤에서 배울 자료형인
 리스트나 튜플에서도 사용 
 a[시작 번호 : 끝 번호]
'''
print(a[0:4])

print(a[0:2], a[5:7], a[12:17])
print(a[19:])
print(a[:5])
print(a[:])
print(a[19:-7])