# FileIOEx05_김세용.py
'''
# with 문과 함께 사용하기
	파일을 열고 닫는 것을 자동으로 처리
'''
with open("foo.txt", "w") as f:
	f.write("Life is too short, you need python")

with open("foo.txt", "r") as f2:
	data = f2.read()
	print(data)