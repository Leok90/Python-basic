#GuGuDanEx02_김세용.py

for i in range(2, 10):
	print("# %d 단	" % i, end="")

print("\n")
print("=" * 62)

for i in range(2, 10):
	for j in range(2, 10):
		print("%d*%d=%2d" %(j, i, j*i), end="	")
	print("\n")
print("-" * 62)