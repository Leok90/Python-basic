# Chap01_02_김세용.py
# 리스트 내포(list comprehension) 표현식

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)