class Car:
    def __init__(self, speed =0, model = "k9", color = "black"):
        self.speed = speed
        self.model = model
        self.color = color

    def __str__(self): #문자열 반환
        result = f"속도 : {str(self.speed)}, 모델 : {self.model}, 색상 : {self.color}"
        return result


myCar = Car()
print(myCar)
print(myCar.__str__())