from person import Person

class Famer(Person):
    def __init__(self, name, age, vegetable):
        super().__init__(name, age, job="famer")
        self.vegetable = vegetable

    def show(self):
        print(f"나는 {self.vegetable}을 키웁니다.")