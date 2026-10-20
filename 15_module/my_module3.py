# 다른 모듈 import
import random
import math

# 전역변수
count = 0

#상수
PI = 3.141592
MAX_SIZE = 100

#자료구조
fruits = ["사과","배","포도"]
student_info = {"name" : "더조은", "age" : 21}

# 함수
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def random_num():
    return random.randint(1,100)

# 클래스
class Student:
    school =  "컴퓨터 대학교"
    def __init__(self, name, age):
        self.name =name
        self.age = age
    # 인스턴스 메서드
    def introduce(self):
        print(f"이름 : {self.name}, 나이 : {self.age}")

    @staticmethod
    def hello():
        print("안녕")

# 클래스 상속
class Tjoeun(Student):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def program(self):
        print(f"{self.name}은 {self.language}로 프로그램 합니다.")

#람다 함수
square = lambda x : x**2