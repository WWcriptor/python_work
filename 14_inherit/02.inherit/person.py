class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.__age = age
        self.job = job

    def hello(self):
        print(f"Hello, I'm {self.name}")

    def updateAge(self, age):
        if age < 0:
            print("나이는 음수일 수 없습니다.")
        else:
            self.__age = age
            print(f"현재 나이는 {self.__age}세 입니다")

    def getAge(self):
        return self.__age


if __name__ == "__main__":
    p1 = Person("김바바", 25)
    p1.hello()
    p1.updateAge(30)

    p1.__age = -7 #p1 객체 안에 __age라는 이름을 가진 인스턴스 변수가 하나 생성됨 / 원래 age는 네임 맹글링 되어 _Person__age로
    # __age = -8 # 전역변수
    print(p1.__age) 
    # print(p1.getAge())
    print(p1._Person__age)
    # print(dir(p1))

# print(__age)