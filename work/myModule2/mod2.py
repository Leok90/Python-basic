# mod2.py 
'''
# 모듈(Modul)
** if __name__ == "__main__": 의 의미

** 직접 이 파일을 실행했을 때는 __name__ == "__main__"이 참이 되어 
	 if문 다음 문장이 수행된다. 
	 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는
	 __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.
'''
PI = 3.141592

class Math: 
    def solv(self, r): 
        return PI * (r ** 2) 

def sum(a, b): 
    return a+b 

# print(PI)

if __name__ == "__main__": 
    print(PI)
    a = Math() 
    print(a.solv(2)) 
    print(sum(PI , 4.4))
