# whileEx04_김세용
# 5회 반복
# idx = 5
# while True:
# ? "커피 1개 판매 후 커피의 양은 %d

idx = 5
while True:
	idx = idx - 1
	print("커피 1개 판매 후 남은 커피의 양은 %d개 입니다." % idx)
	if(idx == 0):
		print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
		break