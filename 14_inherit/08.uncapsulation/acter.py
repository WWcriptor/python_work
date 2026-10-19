from person import Person

class Acter(Person):
    def __init__(self, name, age, film):
        super().__init__(name, age, job="acter")
        self.__film = film

    def introduce(self):
        super().hello()
        print(f"나는 {self.getName()}이고, {self.getAge()}세 입니다")
        print(f"나의 대표작은 {self.__film} 입니다.")

    def getFilm(self):
        return self.__film