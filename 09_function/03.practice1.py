"""
    Q1. 2개의 수를 넣으면 그 사이의 숫자들의 합계 구하기
    Q2. 매개변수에 숫자를 입력하면 숫자만큼 별 찍기
        ex) 3
        *
        **
        ***
"""

def factorial(a, b):
    total =0
    for i in range(a+1, b):
        total += i
    return total

def star(a):
    for i in range(1,a+1):
        for j in range(1,a+1):
            if j <= i:
                print("*", end="")
        print()

def star2(a):
    for i in range(a):
        print("*" *(i+1))

def star_pyramid(a):
    for i in range(1, a*2+1, 2):
        for j in range(int((a*2-i)/2)):
            print(" ", end="")
        for k in range(1, a*2+1):
            if k <= i:
                print("*", end="")
        print()

            

def star_pyramid2(a):
    for i in range(a):
        print(" "*(a-1-i)+"*"*(i*2+1))


star_pyramid2(5)