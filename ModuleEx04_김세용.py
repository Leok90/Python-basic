# moduleEx04_김세용
'''
** if __name__ == "__main__" : 의 의미
** 직접 mod2.py 파일을 실행할 경우
__name__ 변수에는 __main__ 값이 저장된다
하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod2을 import 할 경우
mod2.py의 __name__ 변수에는 mod2.py의 모듈 이름 값 mod2이

# 모듈에서 원하는 함수를 쓰는 방법
'''

from mod2 import *
print(sum(3, 4))
