# ClassEx02_김세용.py << 고객 2명
'''
# 은행관리 시스템V00.
	chk == 1 입금 / == 2 출금
'''
cusBalance01 = 0
cusBalance02 = 0
def Customer01(chk, num, cusBalance):

	if(chk == 1):
		cusBalance += num
	elif(chk == 2):
		cusBalance -= num
	return cusBalance

# 1번 고객 300 입금
cusBalance01 = Customer01(1, 300, cusBalance01)
print(cusBalance01)

# 2번 고객 150 출금
cusBalance02 = Customer01(2, 150, cusBalance02)
print(cusBalance02)

cusBalance02 = Customer01(2, 150, cusBalance02)
print(cusBalance02)