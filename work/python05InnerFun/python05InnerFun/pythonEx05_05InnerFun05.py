# Python 내장함수 dir
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다 .
# 리스트와 딕셔너리 객체의 관련 함수들 반환예
vDir01 = dir([])
vDir02 = dir(())
vDir03 = dir({})

print(vDir01, "\n\n\n" ,vDir02, "\n\n\n" ,vDir03, "\n\n\n" )
