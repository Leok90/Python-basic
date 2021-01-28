# strFunEx01_김세용

# 문자 개수 세기(count)
a = "hobby"

print(a.count('b'))  # 문자열에서 해당 문자의 개수 세기
print(len(a))  # 문자열의 길이


# 위치 알려주기1(find)
a = "Python is the best choice"
print(a.find('b')) # 위치 반환
print(a.find('k')) # 없는 것은 '-1'을 반환


# 위치 알려주기2(index)
a = "Life is too short"
print(a.index('t')) # 인덱스 반환
print(a.index('k')) # 없는 것은 에러를 반환
