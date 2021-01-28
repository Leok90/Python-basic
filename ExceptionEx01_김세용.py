# ExceptionEx01_김세용

try:
	f = open('foo.txt', 'r')
except FileNotFoundError as e:
	print(str(e))
else:
	data = f.readline()
	print(data)
	f.close()