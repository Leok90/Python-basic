# ExceptionEx06
# 오류 만들기
'''
오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면
오류 클래스에 다음과 같은 __str__메서드를 구현해야 한다.
'''
class MyError(Exception):
	def __str__(self):
		return "허용되지 않는 별명입니다."

def say_nick(nick):
	if nick == '바보':
		raise MyError()
	print(nick)

try:
	say_nick("천사")
	say_nick("바보")
except MyError as e:
	print(e)