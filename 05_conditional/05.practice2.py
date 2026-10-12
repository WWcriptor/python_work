"""
    점수를 입력받아 학점 출력
    100점 초과, 음수 입력시 잘못 넣었다고 해야 함
"""

score = int(input("점수를 입력하세요: "))

if score > 100:
    print("점수는 100점을 초과할 수 없습니다.")
elif score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
elif score >= 0:
    print("F학점")
else:
    print("음수로 된 점수는 없습니다.")


if score >= 0 and score <= 100:
    if score >= 90:
        print("A학점")
    elif score >= 80:
        print("B학점")
    elif score >= 70:
        print("C학점")
    elif score >= 60:
        print("D학점")
    else:
        print("F학점")
elif score >100:
    print("100점이 만점입니다.")
else:
    print("음수는 점수가 될 수 없습니다.")

if score > 0 or score < 100:
    print("점수가 잘못됐습니다.")
elif score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")