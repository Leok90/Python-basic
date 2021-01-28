
'''
# 모듈(Module)
** 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법
	- sys.path.append(모듈을 저장한 디렉터리) 사용하기
	- sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여 준다.
	- 만약 파이썬 모듈이 위 디렉터리에 들어 있다면 모듈이 저장된 디렉터리로
		이동할 필요 없이 바로 불러서 사용할 수 있다.
# 명령 프롬프트 창에서는 /, \ 든 상관없지만,
	소스 코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다.
'''
import sys
import mod2

print(sys.path)

sys.path.append("./../myModule3")
print("\n\n", sys.path)

import mod3

print(mod3.sum(1,2))