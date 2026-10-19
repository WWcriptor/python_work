#추상 클래스
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, job = None):
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

    @abstractmethod
    def introduce(self):
        pass

    # 추상 메서드는 자식 클래스에서 오버라이딩 했는가만 검사. 실행 가능함
    # @abstractmethod
    # def info(self):
    #     print("이 메서드는 자기소개 입니다") #but. 잘 사용되지 않음(주로 pass)