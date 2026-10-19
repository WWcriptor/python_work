#생성자 : 객체생성시 호출
#변수를 초기화할 때 사용

class Car:
    def __init__(self,model, color, speed):
        print("생성자 호출")
        self.model = model
        self.color = color
        self.speed = speed

    def output(self):
        print(f"모델 : {self.model}, 색상 : {self.color}, 속도 : {self.speed}")


car1 = Car('sm7','black',20)
car1.output()
print('-'*30)

car2 = Car('e-class','yellow',30)
car2.output()

car2.__init__('sonata','white',50)
car2.output()