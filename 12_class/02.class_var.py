"""
    클래스 변수 : 모든 객체가 변수를 공유
        - class 바로 밑에 선언
        - 사용법 : 클래스이름.변수명
    인스턴스 변수 : 자기자신의 객체에서만 사용
        - 함수안에서 선언 : self.변수명
        - 사용법 : 객체명.변수명
"""

class Car:
    maker = "르노삼성"
    def set1(self):
        self.model = "sm5"
        self.color = "red"
        self.speed = 10

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def output(self):
        print(f"모델 : {self.model}, 색상 : {self.color}, 속도 : {self.speed}")

car1 = Car()
car1.set1()
car1.output()
print("-"*30)

car2 = Car()
car2.set1()
car2.speedUp()
car2.output()
print("-"*30)
car1.output()
print("="*30)

car1.speedDown()
car2.speedUp()
print('-----car1-----')
car1.output()
print('-----car2-----')
car2.output()

print(f"제조사 : {Car.maker}")
print(car1.maker)
print(car2.maker)
Car.maker = "기아"
print(f"제조사 : {Car.maker}")
print("="*30)
print(car1.maker)
print(car2.maker)