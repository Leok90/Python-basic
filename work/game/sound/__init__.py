# C:/Python/game/sound/__init__.py
'''
** 해당 디렉터리의 __init__.py 파일에 __all__ 변수를 설정하고 
import할 수 있는 모듈을 정의해 주어야 한다.

** sound 디렉터리에서 * 기호를 사용하여 import할 경우 이곳에 정의된 
     echo 모듈만 import된다는 의미이다.

※ 착각하기 쉬운데 from game.sound.echo import * 는
     __all__과 상관없이 무조건 import된다. 
	 이렇게 __all__과 상관없이 무조건 import되는 경우는 
	 from a.b.c import * 에서 from의 마지막 항목인 c가 모듈인 경우이다.
'''
#__all__ = ['echo']