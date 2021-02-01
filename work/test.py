#DictionaryEx02V01.py
# 평균 70점 이상 합격
'''
# 조건1]
	01.  없는 번호 입력시 에러메세지

	02.  없는 아이디 입력시 해당ID없음 확인 
	   - in연산자 적용 get 메소드
	   - id 삭제시 xx님 탈퇴확인
	   - del 메소드 적용 삭제후 학생목록 출력

	03. 추가 등록
	   - id 존재시 중복id확인
	   - 연산자적용
'''
import sys

def Systemexit():
	print("학생관리시스템을 종료합니다")
	sys.exit()

def Signout():
	while True:
		x = input('삭제할 ID: ')
		if x in dic.keys():
			del dic[x]
			del idList[x]
			print('Red님 탈퇴확인')
			break
		else:
			print('ID를 다시 입력하세요.')

def Showlist():
	for i in range(len(MenuList)):
		print(MenuList[i], end='\t')
	print('')
	print('-' * 50)
	for i in idList:
		print(i, '\t', dic[i][0], '\t', dic[i][1], '\t', dic[i][2], '\t', sum(dic[i]), '\t', avgScore[i], '\t', passStudent[i])
	print('')

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 9. 메뉴종료 ']
menuChk = ['1','2','3','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];
avgScore = {}
passStudent = {}

dic = {}
deleteIDList = []
idx = 0;

n = len(idList)
for i in range(n):	
	dic[idList[i]] = scoreList[i]	# 딕셔너리 타입으로 학생 정보를 저장
	avgScore[idList[i]] = round(sum(scoreList[i])/3, 2) # 딕셔너리 타입으로 평균점수를 저장
	if avgScore[idList[i]] >= 70:
		passStudent[idList[i]] = '합격'
	elif avgScore[idList[i]] < 70 and 0 < avgScore[idList[i]]:
		passStudent[idList[i]] = '불합격'

while True:
	print('-' * 50)
	print('학생관리시스템v01')
	print('-' * 50)
	for i in range(len(menu)):
		print(menu[i], end='\t')
	print('')
	print('-' * 50)
	
#	try:
	idx = int(input('번호 입력: '))
	if idx == 1:
		Signout()
	elif idx == 2:
		Studentlist()
	elif idx == 3:
		Showlist()
			elif idx == 9:
				break
	#except:
#		print('다시 입력해주세요')
