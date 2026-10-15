from datetime import datetime

# 현재시간
print(datetime.now())

d = datetime(2026, 10, 8, 14, 6, 7)

print(d)

print(f"{d:%Y/%m/%d}")
print(f"{d.hour}:{d.minute}:{d.second}")
print(f"{d:%H:%M:%S}") #두 자리로 들어옴
# H는 24간, I는 12시간제. p:am , pm
print(f"{d:%I:%M:%S %p}")

#일 수 계산
day1 = datetime(2026, 10, 1)
day_num = datetime.now() - day1 
print(day_num)

day_num = (datetime.now() -day1).days
print(f"일 수: {day_num}일")