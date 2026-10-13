"""
    편의점에서 주말 알바의 근무시간을 저장한 튜플
    토요일 오전, 토요일 오후, 일요일 오전, 일요일 오후 근무시간
    Work_hours =(4, 5, 3,4)
    Q1. 주말 동안 일한 총 근무 시간의 합 구하기
    Q2. 일요일 근무 시간만 따로 떼어내어 sun_hours 라는 새로운 튜플 만들어 출력
    Q3. 토요일 오전 근무 시간을 4시간에서 5시간으로 변경
"""

work_hours = (4, 5, 3, 4)
print(sum(work_hours))

sun_hours = work_hours[-2:]
print(sun_hours)

work_hours = (5,) + work_hours[1:]
print(work_hours)