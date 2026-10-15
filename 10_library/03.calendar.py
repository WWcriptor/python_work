import calendar

print(calendar.calendar(2026))
print(calendar.month(2026, 10))

#윤년을 계산해주는 함수
year1 = int(input("년도 입력: "))
if calendar.isleap(year1):
    print(year1,"년은 윤년입니다")
else:
    print(year1, "년은 평년입니다")