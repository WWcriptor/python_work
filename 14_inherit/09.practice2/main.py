"""
    Employee(추상클래스)
        생성자에서 name, emp_id를 초기화 한다
        show_info()는 직원의 이름과 사번을 출력한다.
        calculate_salary()는 추상 메서드이다
    FullTimeEmployee -> Employee 상속받음
        월급(monthly_saraly)을 입력받음
    PartTimeEmployee -> Employee 상속받음
        시급(hourly_wage)과 근무시간(hours)을 입력받음
    main
        직원들을 리스트에 저장하고 반복문으로 급여를 출력한다.
"""

from fullTimeEmployee import FullTimeEmployee as Full
from partTimeEmployee import PartTimeEmployee as Part


employees =[Full("이춘배", "th23245", 3000000), Part("박춘봉", "ph42959", 20000, 10)]

for employee in employees:
    employee.show_info()
    employee.calculate_saraly()