# OptionSplitEx01
string1 = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=030&listType=paper&date=20201223"

string2 = string1.split('?')
print("URL : ", string2[0], "\n")
url1 = string2[0]
QueryString = string2[1].split('&')
print("QueryString : ")
for i in range(len(QueryString)):
	print(QueryString[i])
print("\nQueryString의 개수는 : ", len(QueryString))