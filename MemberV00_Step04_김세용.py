#MemberV00_Step04_김세용.py

def menuDesign():	# 메뉴 디자인 함수
	print("\n{0:=^44}\n".format(" 메뉴선택 "))
	for i in range(len(menu)):
		print(menu[i], end=" ")
	print("\n\n" + "=" * 48)
	print("")

def menuSel():	# 메뉴번호선택 함수
	number = int(input("\n\t 메뉴의 번호를 선택해주세요.  "))
	print("")
	return number

def memSignIn():	# 회원가입 함수
	memTemp = []
	print("\t", menu[0]) 
	for i in range(len(itemList)): # ID, PWD, NAME, EMAIL, PHONE, ADDRESS 입력 받기
		temp = input("\t %s : " % itemList[i])
		memTemp.append(temp)	# 임시 리스트 memTemp에 회원정보 입력
	memList.append(memTemp)	# memList에 임시 리스트를 추가
	memTemp = []  # 다른 회원정보를 받기 위해서 임시 리스트를 비워주기
	print("\t ", end="")
	print(memList)
	print("\t 현재 회원수는 %d명입니다." % len(memList)) 

def printMem():
	if len(memList) > 0:		# 회원정보가 1개 이상 있을 경우에만 출력
		print("\t", menu[2], end="\n\n")
		print("-" * 100)
		for i in itemList:
			print("%15s" % i, end="") # ID, PWD, NAME, EMAIL, PHONE, ADDRESS 출력
		print("")
		print("-" * 100)
		for i in range(len(memList)): # 회원수만큼 반복
			for j in memList[i]:		# 회원의 정보를 출력
				print("%15s" % j, end="")
			print("")
		print("")

def memLog():
	cnt = 0
	ID = input("\tID를 입력하세요 : ")
	PWD = input("\tPassward를 입력하세요 : ")
	for i in range(len(memList)):
		if ID in memList[i][0] and PWD in memList[i][1]:
			cnt = cnt + 1
	if cnt == 1:
		print("\n\t\t로그인 성공하였습니다.")
	else:
		print("\n\t\tID나 Password를 잘못 입력하셨습니다.")


menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
memList = []
ID = 0
PWD = 0

menuDesign()

while True:
	number = menuSel()
	if number == 9:		# 9를 입력한 경우 메뉴를 종료
		print("\t\t메뉴를 종료합니다\n")
		break	    
	elif number == 1:   # 1을 입력한 경우 회원가입
		memSignIn()
	elif number == 3:		# 회원목록
		printMem()
	elif number == 2:		# 로그인
		memLog()
