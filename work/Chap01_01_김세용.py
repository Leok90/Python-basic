# Chap01_01_김세용.py

# Q2
sum = 0
i = 1
while i <= 1000:
	if i % 3 == 0:
		sum = sum + i
	i = i + 1
print("Q2")
print("3의 배수의 합은 %d 입니다.\n\n" % sum)


# Q3
i = 0
print("Q3")

while True:
	i = i + 1
	print("*" * i)
	if i == 5:
		break
print("\n")


# Q4
print("Q4")
for i in range(100):
	print("%d, " % (i+1), end="")
print("\n")


# Q5
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
print("Q5")

for i in range(len(score)):
	sum = sum + score[i]
	avg = sum / len(score)
print("A 학급의 평균 점수는 :", avg)

