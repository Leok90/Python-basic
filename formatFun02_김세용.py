# formatFun02_김세용

str01 = "My Name is {}".format('Kim')
int01 = "{1} X {0} = {2}".format(10, 20, (10+20))

print(str01)
print(int01)

str01 = "My Name is {}".format('Kim')
int01 = "{idx1} X {idx2} = {idx3}".format(idx2=10, idx1=20, idx3=(10+20))

print(str01)
print(int01)