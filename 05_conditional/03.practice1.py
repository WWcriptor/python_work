"""
    1.사용자로부터 정수를입력받아 짝수인지 홀수인지를 판별

    2. 2개의 정수를 입력받아 큰 값과 작은 값을 판별하여 출력
        n, m 입력 -> 큰 값:n, 작은 값:m
"""

num = int(input("정수를 입력하세요: "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")


num1 = int(input("첫 번쨰 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

if num1 > num2:
    print(f"큰 값 : {num1}, 작은 값 : {num2}")
if num2 > num1:
    print(f"큰 값 : {num2}, 작은 값 : {num1}")

if num2 > num1:
    num1, num2 = num2, num1

print(f"큰 값 : {num1}, 작은 값 : {num2}")