"""
    무한 반복으로 구구단 중 출력할 단수를 입력받아 출력
    출력 후 구구단을 계속할 것인지 확인 y: 계속
"""

while True:
    num = int(input("몇 단을 출력할까요?: "))
    for i in range(1,10):
        print(f"{num}*{i}={num*i}")
    command = input("계속하려면 'y'를 입력하세요:")
    if command.lower() != "y":
        print("프로그램 종료")
        break

