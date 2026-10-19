from person import Person

class Famer(Person):
    def __init__(self, name, age, vegetable):
        super().__init__(name, age, job="famer")
        self.__vegetable = vegetable

    def introduce(self):
        super().hello()
        print(f"나는 {self.getName()}이고, {self.getAge()}세 입니다")
        print(f"나는 {self.__vegetable}을 키웁니다.")

    def getVegetable(self):
        return self.__vegetable
    