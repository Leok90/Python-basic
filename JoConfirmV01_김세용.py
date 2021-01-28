## JoConfirmV01_김세용.py
'''
조건 ]
1. 실행시에 4인 이상의 이름을 입력받는다.
2. 4인 이하라면? "4인 이상을 입력하세요 : "
3. 보라돌이 뽀오 나나 뚜비
'''

import sys

args = sys.argv[1:]
n = len(args)
if n >= 4:
	for i in args:
		print(i,"  ", end="")
else:
	print("4인 이상을 입력하세요.")
print("")