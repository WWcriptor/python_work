"""
* 함수 : 클래스 바깥쪽에 독립적으로 존재. 이름만으로 바로 호출 가능
* 메서드 : 클래스 내부에 정의되어 있고, 객체를 통해 호출하는 함수

def 함수명(매개변수들):
    실행문
    return

"""

#매개변수가 없고 반환값이 없는 함수

def func():
    print("서울특별시 강남구")
    print("삼오빌딩 704호")


func()

print("-"*20)

def add1():
    a = 3+8
    print(a)

print(add1())

#매개변수가 없고 반환값이 있는 함수

def add2():
    a = 3+8
    return a

print(add2())

print("-"*20)

#매개변수가 있는 함수
def multi(x,y):
    result = x*y
    print(f"{x}*{y}={result}")

multi(4,3)

def multi2(x,y):
    result = x*y
    return result

print(multi2(4,8))

def star(n):
    for i in range(n):
        print("*", end="")
    print()

star(5)