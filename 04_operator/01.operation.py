#산술 연산자
# // : 몫 연산자
# ** : 지수 연산자
num1 = int(input("정수를 입력하세요 : "))
num2 = int(input("정수를 입력하세요 : "))

result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2 #정수 / 정수 = 실수

print(f"{num1} + {num2} = {result1}")
print(f"{num1} - {num2} = {result2}")
print(f"{num1} * {num2} = {result3}")
print(f"{num1} / {num2} = {result4}")

result5 = num1 % num2
print(f"{num1} % {num2} = {result5}")

result6 = num1 // num2
print(f"{num1} // {num2} = {result6}")

result7 = num1 ** 3
print(f"{num1}^3 = {result7}")