# private : 외부에서 접근 못하게 막음
class Car:
    def __init__(self, speed =0, color="gray",model="K7",maker="KIA"):
        self.speed = speed
        self.color = color
        self.model = model
        self.__maker = maker

    def output(self):
        print("속도 :", self.speed)
        print("색상 :", self.color)
        print("모델 :", self.model)
        print("제조사 :", self.__maker)

    def getMaker(self):
        return self.__maker

    def setMaker(self, maker):
        self.__maker = maker


car = Car()
car.output()

print(car.speed)
print(car.model)
print(car.getMaker())
print('-'*30)

car.speed = 50
car.__maker = "samsung"
car.output()