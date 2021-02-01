# Python 내장함수 range
# for문과 함께 자주 사용되는 함수
# 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴
# 인수가 하나일 경우, 0부터 시작
# 인수가 2개일 경우, 시작 숫자와 끝 숫자, 단, 끝 숫자는 해당 범위에 포함되지 않는다
# 인수가 3개일 경우, 세 번째 인수는 숫자 사이의 거리

vRange01 =  list(range(5))
vRange02 =  list(range(5, 10))
vRange03 =  list(range(1, 10, 2))
vRange04 =  list(range(0, -10, -1))

print(vRange01, " / " , vRange02)
print(vRange03, " / " , vRange04)
