# whileExamStep01_김세용.py
# 여러 가지 선택지 중 하나를 선택해서 입력받는 예제

# 여러 줄 문자열을 적는 방법 ''' '''
prompt = '''
1. Add
2. Del
3. List
4. Quit
'''

number = 0
while number !=4:
	print(prompt)
	number = int(input('Enter number: '))