# Python 내장함수 open
# open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 리턴
# b는 w, r, a와 함께 사용된다.
#  생략되면 기본값으로 읽기 모드인 r을 갖게 된다.
#vOpen01 = open("read_mode.txt", "rb")
vOpen02 = open("read_mode.txt", "r")

line = vOpen02.readline()
print(line)
vOpen02.close()