"""
    사용자로부터 두 수를 입력받고, 연산자도 입력을 받음
    연산 결과를 출력
    연산 종류는 +, -, *, /, //, %, **    
"""

num1 = int(input("첫 번쨰 숫자를 입력하세요: "))
num2 = input("두 번째 숫자를 입력하세요: ")

operator = input("연산자를 입력하세요: ")

result = 0

if operator == "+" or operator == "-":
    result = num1 + int(operator+num2)
elif operator == "*":
    result = num1 * int(num2)
elif operator == "/":
    result = num1 / int(num2)
elif operator == "//":
    result = num1 // int(num2)
elif operator == "%":
    result = num1 % int(num2)
elif operator == "**":
    result = num1 ** int(num2)


print(num1, operator, num2, "=", result)

"""
    숫자를 입력 받아
    양수 음수 여부와 홀짝 여부를 출력
"""

num = int(input("숫자를 입력하세요: "))
if num != 0:
    m = "양수" if num >= 0 else "음수"
    n = "짝수" if num % 2 == 0 else "홀수"

    print(f"{num}은 {m}이면서 {n}입니다")
else:
    print("0입니다")