# ExceptionEx04
# 오류 일부러 발생시키기
class Bird:
	def fly(self):
		print('날다')
		raise NotImplementedError

class Eagle(Bird):
	def fly(self):
		pass

eagle = Eagle()
eagle.fly()