#MemberV00_Step01_김세용.py

menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
memList = []


print("\n{0:=^44}\n".format(" 메뉴선택 "))
for i in range(len(menu)):
	print(menu[i], end=" ")
print("\n\n" + "=" * 48)
print("")

while True:
	number = input("\t메뉴의 번호를 선택해주세요.  ")
	print("")
	if number == '9':		# 9를 입력한 경우 메뉴를 종료
		print("\t\t메뉴를 종료합니다\n")
		break
	
	for i in range(len(menu)):    
		if number == menuChk[i]:   # number와 같은 menuChk의 인덱스 i를 찿아서
			print("\t\t%s Algorithm Chk\n" % menu[i]) # 인덱스 i에 맞는 menu값 출력
	