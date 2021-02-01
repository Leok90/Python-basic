# ClassEx08_김세용.py
'''
# 생성자 (Constructor)
# 상속 : 일반화
** 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에
	상속할 클래스 이름을 넣어주면 된다.
형식 ] class 클래스 이름(상속할 클래스 이름)
'''
class FourCal:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def sum(self):
		result = self.first + self.second
		return result

	def sub(self):
		result = self.first - self.second
		return result

	def mul(self):
		result = self.first * self.second
		return result

	def div(self):
		result = self.first / self.second
		return result

class MoreFourCal(FourCal):
	pass

a = MoreFourCal(4, 2)

print(a.first, " + ", a.second, " = ", a.sum())
print(a.first, " - ", a.second, " = ", a.sub())
print(a.first, " * ", a.second, " = ", a.mul())
print(a.first, " / ", a.second, " = ", a.div())