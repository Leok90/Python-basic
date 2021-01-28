# ifEx04

# 조건
# 사용자로부터 id와 pwd를 입력 받는다.
# input(id 입력하세요) / input(pwd 입력하세요)
# vID == "Orange" and vPWD == "1234"
# -> ? 회원 인증 성공
# vID == "Orange" or vPWD == "1234"
# -> ? 아이디 또는 비밀번호 확인
# 그렇지 않으면 인증실패!!


vID = input("id를 입력하세요 : ")
vPWD = input("pwd를 입력하세요 : ")

if(vID == "Orange" and vPWD == "1234"):
	print("회원 인증 성공")
elif(vID == "Orange" or vPWD == "1234"):
	print("아이디 또는 비밀번호 확인")
else:
	print("인증실패!!")