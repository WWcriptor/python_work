from datetime import date

print(date.today())

d = date(2026, 10, 8)
print(d)

print(f"{d.year}/{d.month}/{d.day}")

print(f"{d:%Y/%m/%d}")
print(f"{d:%y/%m/%d}")