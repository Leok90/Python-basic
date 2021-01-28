#foodOrderV01.py

foodOrder = ['pizza', 'pork', 'potato', 'cokeZero']
foodPrice = [12000, 15000, 7000, 1000]
total = 0;
i = 0;

for i in foodPrice:
	total = i + total
discount = total*0.85

print(" >>> 음식주문 <<< ")
print("=" * 30)
for i in range(len(foodOrder)):
	print("  %-10s :  %5d" % (foodOrder[i], foodPrice[i]))
print("-" * 30)
print("토탈주문금액 : %5d" % total)
print("15%% 할인카드 : %5d" % discount)