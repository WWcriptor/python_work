from person import Person

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def introduce(self):
        print(f"나는 {self.language}언어로 프로그래밍 합니다.")

    def show_vari(self):
        print("이름 :", self.name)