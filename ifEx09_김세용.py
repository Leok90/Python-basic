# ifEx09_김세용.py
# 사용자로부터 점수를 입력받는다.
# 60점 이상이면 success 아니면 failure
# 조건부 표현식으로 결과 확인

score = int(input("점수를 입력하세요 : "))

message = "success" if score >= 60 else "failure"
print(message)