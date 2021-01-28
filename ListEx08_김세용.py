# ListEx08_김세용
# 리스트 요소 제거(remove)_첫 번째 3만 제거
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

print("-" * 15)

# 리스트 요소 끄집어내기(pop)_맨 마지막 요소를 돌려주고 그 요소는 삭제
a = [1, 2, 3]
print(a.pop())
print(a)
print("-" * 15)

# a.pop(1)은 a[1]의 값을 끄집어낸다.
a = [1, 2, 3]
a.pop(1)
print(a)
print("-" * 15)