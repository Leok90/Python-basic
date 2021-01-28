# 예외 처리
'''
   - 프로그램을 중단하고 오류 메시지 출력 방지.
   - try, except를 사용해서 예외적으로 오류를 처리.
   - FileNotFoundError : 없는파일 불러올때 발생 Error
   - ZeroDivisionError: 0으로 다른 숫자를 나누는 경우
   - IndexError: 없는 Index 사용경우

 ** 오류 예외 처리 기법
 try, except문
 형식 ] 
 try:
    ...
except [발생 오류[as 오류 메시지 변수]]:

위 구문을 보면 [ ] 기호를 사용하는데, 
이 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다. 

즉 except 구문은 다음 3가지 방법으로 사용할 수 있다.

1. try, except만 쓰는 방법
try:
    ...
except:
    ...

2. 발생 오류만 포함한 except문
try:
    ...
except 발생 오류:
    ...

3. 발생 오류와 오류 메시지 변수까지 포함한 except문

try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...

** try .. finally
   finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 
   보통 finally절은 사용한 리소스를 close해야 할 때에 많이 사용한다.

** 여러개의 오류처리하기
try:
    ...
except 발생 오류1:
   ... 
except 발생 오류2:
   ...

** 오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

** 오류 일부러 발생시키기
   - raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.

※ NotImplementedError는 파이썬 내장 오류로, 
	꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 
	일으키기 위해 사용한다.

** 예외 만들기
   - 예외는 다음과 같이 파이썬 내장 클래스인 Exception 클래스를 
      상속하여 만들 수 있다.

class MyError(Exception):
    pass

'''
try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.readline()
    print(data)
    f.close()
