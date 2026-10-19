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
