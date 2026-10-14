"""
    Q1. 매개변수로 2개의 숫자와 연산자를 입력받아 출력
    Q2. 국어, 영어 점수를 사용자로부터 입력받아 함수로 평균을 입력받아 평균의 학점을 return 하기
    Q3. 로또를 함수로
"""

def operator(num1, num2, op):
    if op == "+":
        return num1 + num2

    if op == "-":
        return num1 - num2

    if op == "*":
        return num1 * num2

    if op == "/":
        if num2 != 0:
            return num1/num2
        else:
            return "0으로는 나눌 수 없습니다"


num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))
op = input("연산자: ")

print(operator(num1, num2, op))

def grade(avg):
    if avg >=90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >=70:
        grade = "C"
    elif avg >=60:
        grade ="D"
    else:
        grade="F"

    return grade

kr = int(input("국어 점수: "))
en = int(input("영어 점수: "))

avg = (kr + en)/2

print(grade(avg))

import random

def lotto():
    nums = set()
    while len(nums) != 6:
        nums.add(random.randint(1,45))

    result = sorted(nums)
    return result

print(lotto())

def password():
    words = None
    while True:
        words = input("새로운 비밀번호를 입력하세요: ")

        if len(words) < 8:
            print("오류. 비밀번호가 규칙에 맞지 않습니다.")
            continue

        if not words.isalnum():
            print("오류. 비밀번호가 규칙에 맞지 않습니다.")
            continue

        print("비밀번호가 생성 되었습니다.")
        break
    return words

print(password())
