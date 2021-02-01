# FunEx06_김세용.py
'''
키워드 파라미터 kwargs
키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙인다.

** 딕셔너리로 만들어져서 출력
	매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고
	모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.

# 여기에서 kwargs는 keyward arguments의 약자이며
	args와 마찬가지로 관례적으로 사용한다.
'''

def print_kwargs(**kwargs):
	print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)