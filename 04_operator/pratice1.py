"""
문제
파운드(lb)와 킬로그램(Kg)을 상호 변환하는 프로그램 만들기

kg = lb*0.453492
lb = kg*2.204623
"""

gram = input("파운드와 킬로그램 중 어느 것인가요? : ")
if gram == "파운드":
    num = float(input("몇 파운드 인가요?(숫자만 입력) : "))
    num2 = num * 2.204623
    print(f"{num}lb = {num2:.2f}Kg")
elif gram == "킬로그램":
    num = float(input("몇 킬로그램 인가요?(숫자만 입력) : "))
    num2 = num * 0.453492
    print(f"{num}Kg = {num2:.2f}lb")
else:
    print("잘못 입력했습니다.")

