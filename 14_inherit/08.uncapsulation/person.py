#추상 클래스
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, job = None):
        self.__name = name
        self.__age = age
        self.__job = job

    # getter 메소드 ---- 조회용

    def getName(self):
        return self.__name

    def getAge(self):
            return self.__age

    def getJob(self):
        return self.__job


    # setter 메소드 ---- 수정용

    def setAge(self, age):
        if age < 0:
            print("나이는 음수일 수 없습니다.")
        else:
            self.__age = age
            print(f"[{self.__name}]의 나이가 {self.__age}세로 업데이트 되었습니다.")

    def setJob(self, job):
         self.__job = job

    def hello(self):
        print(f"Hello I'm {self.__name}.")

    @abstractmethod
    def introduce(self):
        pass