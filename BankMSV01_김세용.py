class BankV01:
	setBankBalance = 100000
	
	def __init__(self, number, name, cusBalance):
		self.cusBalance = cusBalance
		self.number = number
		self.name = name

bankInfo = [ ["BANK001", "서건호"],
							["BANK002", "김병태"],
							["BANK003", "신진영"],
							["BANK004", "이선규"],
							["BANK005", "김대은"],
							["BANK006", "양동혁"],
							["BANK007", "최창희"] ];
vBalance = [10000, 20000, 30000, 40000, 50000, 60000, 70000];
cusList = []


for i in range(len(bankInfo)):
	cusTemp = BankV01(bankInfo[i][0], bankInfo[i][1], vBalance[i])
	BankV01.setBankBalance += vBalance[i]
	cusList.append(cusTemp)


def bankPrintInfo():
	print("")
	print("\t■ 은행 관리 프로그램 V01 ■")
	print("-" * 60)
	print("{:^15}{:^15}{:>15}".format("No", "이름", "잔고"))
	print("-" * 60)

bankPrintInfo()


for idx in range(len(cusList)):
	print("{0:^15}".format(cusList[idx].number), end="")
	print("{0:^15}".format(cusList[idx].name), end="")
	print("{0:>15,d}  ".format(cusList[idx].cusBalance), end="")
	print("")

print("")
print("{0:>15}{1:>10,d} ".format("은행잔고 :", BankV01.setBankBalance))
print("=" * 60)

