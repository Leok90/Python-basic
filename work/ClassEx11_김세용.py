
class Family:
	vI = 10
	def __init__(self, first):
		self.vI01 = first

a = Family(10)

print(id(Family.vI))

Family.vI += 1
a.vI01 += 2

b = Family(3)
a.vI += 4
b.vI01 += 5
b.vI += 6

print(id(Family.vI), "\n", id(a.vI), "\n", id(a.vI01), "\n", id(b.vI), "\n", id(b.vI01))

print("Family.vI : ", Family.vI)
print("a.vI : ", a.vI)
print("a.vI01 : ", a.vI01)
print("b.vI : ", b.vI)
print("b.vI01 : ", b.vI01)