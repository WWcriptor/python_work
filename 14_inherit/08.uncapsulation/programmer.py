from person import Person

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, job="programmer")
        self.__language = language

    def introduce(self):
        super().hello()
        print(f"나는 {self.getName()}이고, {self.getAge()}세 입니다")
        print(f"나는 {self.__language}언어를 사용할 줄 압니다.")

    def getLanguage(self):
        return self.__language