"""
    20세 이상 : 성인
    15~19세 : 청소년
    15세 미만 : 어린이
"""

age = int(input("나이를 입력하세요: "))

if age > 19:
    print("adult")
elif age >=15:
    print("teenager")
else:
    print("child")


if age <= 19:
    if age >= 15:
        print("teenager")
    else:
        print("child")
else:
    print("adult")