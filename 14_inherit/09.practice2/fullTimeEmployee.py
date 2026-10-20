from employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_saraly):
        super().__init__(name, emp_id)
        self.__monthly_saraly = monthly_saraly

    def calculate_saraly(self):
        print(f"{self.getName()}의 월급은 {self.__monthly_saraly}원입니다")