# whileFormat013 샘플 답안

fruit_list = ['Apple', 'Melon', 'Grape', 'StrawBerry']
user_input = int(input('반복할 숫자를 입력하세요 : '))
Apple_count = 0
Melon_count = 0
Grape_count = 0
StrawBerry_count = 0
for i in range(1, user_input+1):
	print(i, end=' ')

	if i % 3 == 0:
		print(fruit_list[0], end=' ')
		Apple_count = Apple_count + 1

	if i % 4 == 0:
		print(fruit_list[1], end=' ')
		Melon_count = Melon_count +  1

	if i % 5 == 0:
		print(fruit_list[2], end=' ')
		Grape_count = Grape_count + 1

	if i % 8 == 0:
		print(fruit_list[3], end=' ')
		StrawBerry_count = StrawBerry_count + 1

	print('')

print('\n== << Fruit Coount List >> ==\n')

print('1. Apple\t%d회' % Apple_count)
print('2. Melon\t%d회' % Melon_count)
print('3. Grape\t%d회' % Grape_count)