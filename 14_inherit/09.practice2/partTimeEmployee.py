from employee import Employee

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_wage, hours):
        super().__init__(name, emp_id)
        self.__hourly_wage = hourly_wage
        self.__hours = hours
        self.__pay = self.__hourly_wage * self.__hours

    def calculate_saraly(self):
        print(f"시간당 급여는 {self.__hourly_wage}원, 일한 시간은 {self.__hours}시간 이므로, 급여는 총 {self.__pay}원 입니다")