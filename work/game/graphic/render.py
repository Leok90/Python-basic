# render.py
'''
relative 패키지 << pythonEx05_03Package07.py Chk
** graphic 디렉터리의 render.py 모듈이 
     sound 디렉터리의 echo.py 모듈을 사용하고 싶다면

** relative한 접근자에는 다음과 같은 것이 있다.
   .. – 부모 디렉터리
   . – 현재 디렉터리
'''
# from game.sound.echo import echo_test
from ..sound.echo import echo_test

def render_test():
    print ("render")
    echo_test()