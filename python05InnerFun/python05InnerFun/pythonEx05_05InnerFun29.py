# Python 내장함수 sorted
# 입력값을 정렬한 후 그 결과를 리스트로 리턴
# 리스트 자료형의 sort 함수는 리턴값 없다.
a = [3, 1, 2]
vSorted01 = sorted([3, 1, 2])
vSorted02 = sorted(['a', 'c', 'b'])
vSorted03 = sorted("zero")
vSorted04 = a.sort()

print(vSorted01, " / " , vSorted02)
print(vSorted03, " / " , vSorted04)
