'''
# isinstance
# isinstance(object, class )는 
	첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
'''
class Person: pass
a = Person()

b = 3

print(isinstance(a, Person))
print(isinstance(b, Person))

