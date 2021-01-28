# 사번, 이름, 입사일, 급여
# 계약직, 정규직
# 사번 1번째
# T, t << 계약직
# R    << 정규직
#EmployeeV00.py

TName = ["구분","사원명","입사일","급여"]

empInfo = [
	['T160501',"캔디","2016-05-10"],
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]

empPayTable = [
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]
]

# empInfo 원소 개수만큼 job_type 리스트 빈공간을 생성
job_type = []
for i in range(len(empInfo)):
	job_type.append(0)

for i in range(len(TName)):
	print("%-8s" % TName[i], end="")
print('\n' + '-' * 40)

# T, R값을 슬라이싱으로 job_type에 저장
for i in range(len(empInfo)):
	job_type[i] = empInfo[i][0][0].upper()

# T, R값에 따라서 계약직, 정규직을 구분하여 출력
for i in range(len(empInfo)):
	if job_type[i] == 'T':
		print("계약직\t", empInfo[i][1], "\t", empInfo[i][2], "\t", empPayTable[i][0]*empPayTable[i][1], "\n", end="")
	else:
		print("정규직\t", empInfo[i][1], "\t", empInfo[i][2], "\t", empPayTable[i][0]*empPayTable[i][1], "\n", end="")
