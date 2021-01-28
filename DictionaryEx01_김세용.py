# DictionaryEx01_ 김세용.py
'''
대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 갖고 있는데,
 이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다.
 파이썬에서는 이러한 자료형을 딕셔너리(Dictionary)라고 한다.
 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형
'''

a = {1: 'hi'}
print(a)
print("-" * 15)
a = { 'a' : [1,2,3]}
print(a)

print("-" * 15)

# 딕셔너리 쌍 추가, 삭제하기
'''
딕셔너리 쌍 추가하기
a[2] = 'b' 와 같이 입력하면 딕셔너리 a에 Key와 Value가 각각
 2와 'b'인 2 : 'b' 라는 딕셔너리 쌍이 추가
 '''