#  rangeEx08

result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)

'''
for x in range(2,10)   # 2, 3, 4, ... 9
	for y in range(1,10)   # 1 2 3 ... 9
		x*y
'''