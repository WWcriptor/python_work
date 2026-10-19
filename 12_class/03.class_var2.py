class HelloWorld:
    msg = 'Python' #클래스 변수
    def setEng(self):
        self.msg = "Hello Python" #인스턴스 변수

    def setKr(self):
        self.msg = "안녕하세요 파이썬" #인스턴스 변수

    def setLocal(self):
        msg = "파이썬 수업" #지역변수(메서드 안에서만 사용 가능)
        print(msg)

    def sayHello(self):
        print(HelloWorld.msg) #클래스변수 호출
        print(self.msg)
        # print(msg) #오류! 지역변수가 선언된 곳에서만 호출 가능
    
hello1 = HelloWorld()
hello1.sayHello() #클래스 변수 호출
print("-"*30)

hello1.setEng()
hello1.sayHello()
print("-"*30)

hello1.setKr()
hello1.sayHello()

hello1.setLocal()