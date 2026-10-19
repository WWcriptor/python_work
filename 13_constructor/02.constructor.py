class Car:
    def __init__(self, speed =0, color ='black', model='e-class'):
        self.speed = speed
        self.color = color
        self.model = model

    def output(self):
        print(f'모델 : {self.model}, 색상 : {self.color}, 속도 : {self.speed}')

car1 = Car(30)
car1.output()

car2 = Car(model="Sonata")
car2.output()

car3 = Car(60, 'green', 'K9')
car3.output()

car3.__init__(50, 'white', 'Sy')
car3.output()