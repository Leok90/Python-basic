#MemberV00_Step02_김세용.py

menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
memList = []
memTemp = []		# 회원 1명 분의 회원정보를 저장할 임시 리스트

print("\n{0:=^44}\n".format(" 메뉴선택 "))
for i in range(len(menu)):
	print(menu[i], end=" ")
print("\n\n" + "=" * 48)
print("")

while True:
	number = int(input("\t 메뉴의 번호를 선택해주세요.  "))
	print("")
	if number == 9:		# 9를 입력한 경우 메뉴를 종료
		print("\t\t메뉴를 종료합니다\n")
		break	    
	elif number == 1:   # 1을 입력한 경우 회원가입
		print("\t", menu[0]) 
		for i in range(len(itemList)): # ID, PWD, NAME, EMAIL, PHONE, ADDRESS 입력 받기
			temp = input("\t %s : " % itemList[i])
			memTemp.append(temp)	# 임시 리스트 memTemp에 회원정보 입력
		memList.append(memTemp)	# memList에 임시 리스트를 추가
		memTemp = []  # 다른 회원정보를 받기 위해서 임시 리스트를 비워주기
		print("\t ", end="")
		print(memList)
		print("\t 현재 회원수는 %d명입니다." % len(memList)) 
		