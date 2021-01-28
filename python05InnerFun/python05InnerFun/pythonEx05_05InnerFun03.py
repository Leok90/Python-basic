# Python 내장함수 any
# 하나라도 참이 있을 경우 True, 
# x가 모두 거짓일 경우에만 False
vAny01 = any([1, 2, 3, 0])
vAny02 = any([0, ""])

print(vAny01," / ",vAny02)