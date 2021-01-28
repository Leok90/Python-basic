
'''
setdata 메서드의 첫 번째 매개변수 self에는 setdata 메서드를 호출한
	객체 a가 자동으로 전달

# 메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은
	파이썬만의 독특한 특징이다.
	예를 들어 자바 같은 언어는 첫 번째 매개변수 self가 필요없다.
'''

class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second

a = FourCal()
a.setdata(4, 2)

print(a.first)
print(a.second)
print(type(a))