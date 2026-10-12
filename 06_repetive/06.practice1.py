"""
    숫자 2개를 입력받아 합계 구하기. 무한 반복
    사용자가 첫 번쨰 값에 0을 넣으면 종료
"""

while True:
    num1 = int(input("첫 번째 값을 입력(종료하려면 0): "))
    if num1 == 0:
        break
    num2 = int(input("두 번째 값을 입력: "))

    print(f"{num1}+{num2}={num1+num2}\n")

print("프로그램이 종료되었습니다.")