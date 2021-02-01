'''
sys 모듈을 사용하려면 아래 예의 import sys처럼
	import 명령어를 사용해야 한다

PythonFile.py	a				b				c
argv[0]			argv[1]		argv[2]	argv[3]
'''

import sys

args = sys.argv[1:]
print(args)

for i in args:
	print(i)

print(len(args))