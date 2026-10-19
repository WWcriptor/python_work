from person import Person

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, job="programmer")
        self.language = language

    def introduce(self):
        super().hello()
        print(f"나는 {self.language}언어를 사용할 줄 압니다.")

    def info(self):
        print("프로그래머")