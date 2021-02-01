
'''
# Override / super()
	클래스 변수 : 모든 객체가 공유

** 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를
	선언하여 생성한다.
** 클래스 변수는 클래스이름.클래스 변수로 사용할 수 있다.
	
		Method[Class]			Stack			Heap
		class Family:				변수				a = Family()
			lastname = "김"							b = Family()
'''
class Family:
	lastname = "김"

a = Family()
b = Family()

print(Family.lastname)
print(a.lastname)
print(b.lastname)

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))