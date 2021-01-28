# FruitListEx01_김세용.py

Fruit = ['Apple', 'Melon', 'Grape', 'StrawBerry']
i = 0
k = 0
c = 0
n = [3, 4, 5, 8]
Fruit_count = [0, 0, 0, 0]
num = int(input("반복될 숫자를 입력하세요. :"))

while i < num:
	i = i + 1		# i는 나누어지는 수
	print("%d. " % i, end="")
	for j in range(1, i+1):	# j는 나누는 수
		if i % j == 0:	
			for k in range(len(n)):	# k는 리스트 n의 인덱스
				if j == n[k]:	# 나누는 수와 n의 원소가 같을 경우
					print("%s" % Fruit[k], end=" ")	# 인덱스 k를 활용
					Fruit_count[k] += 1
	print("")
print("== << Fruit Count List >> ====")
for i in range(len(Fruit)):
	print("%d. %s	%d회" % (i+1, Fruit[i], Fruit_count[i]))

