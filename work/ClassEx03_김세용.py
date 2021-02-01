# ClassEx03_김세용

class Customer:
	def __init__(self):		# 생성자
		self.cusBalance = 0  # member variable

	def deposit(self, num): # 입금, self는 객체를 의미
		self.cusBalance += num	# 클래스 안의 함수는 메소드로 불림
		return self.cusBalance	# member method

	def withdraw(self, num): # 출금
		self.cusBalance -= num	# member method
		return self.cusBalance

cus01 = Customer()		# 객채
cus02 = Customer()

print(cus01.deposit(300))
print(cus01.withdraw(150))
print(cus02.deposit(400))
print(cus02.withdraw(150))