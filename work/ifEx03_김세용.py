# ifEx03_김세용.py
# 사용자로부터 점수를 입력 받는다.
# 90점 이상이면 : A 학점
# 80점 이상이면 : B 학점
# 70점 이상이면 : C 학점

vId = input("점수를 입력하세요 : ")

if(vId >= "90"):
	print("A 학점")
elif(vId >= "80"):
	print("B 학점")
elif(vId >= "70"):
	print("C 학점")