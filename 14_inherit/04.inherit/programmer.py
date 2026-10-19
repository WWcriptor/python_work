from person import Person
from employee import Employee

class Programmer(Person, Employee):
    def __init__(self, name, age, language, emp_id, salary):
        Person.__init__(self, name, age, job="Programmer")
        Employee.__init__(self, emp_id, salary)
        self.language = language

    def introduce(self):
        print(f"나는 {self.language}언어로 프로그래밍하는 {self.name}입니다.")
        print(f"나이는 {self.getAge()}세 이고, 사번은 {self.emp_id}입니다")
