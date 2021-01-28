# DictionaryEx03_김세용.py

'''
또 한 가지 주의해야 할 사항은 Key에 리스트는 쓸 수 없다는 것이다.
하지만 튜플은 Key로 쓸 수 있다.
딕셔너리의 Key로 쓸 수 있느냐 없느냐는 Key가 변하는 값인지
변하지 않는 값인지에 달려 있다.
리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다.
다음 예처럼 리스트를 Key로 설정하면 리스트를 키 값으로 사용할 수 없다는
오류가 발생한다.
따라서 딕셔너리의 Key값으로 딕셔너리를 사용할 수 없음은 당연하다.
단, Value에는 변하는 값이든 변하지 않는 값이든 상관없이 아무 값이나 넣을 수 있다.
'''

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(dic['name'])
print(dic['phone'])