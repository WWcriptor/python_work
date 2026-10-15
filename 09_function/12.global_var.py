a=20 #전역변수 : 선언된 이후로는 어디서든 사용 가능

def fun1():
    a = 10
    print("func1()의 a =", a)
    print("fun1()에서 전역변수 a:", globals()['a'])

# print(a) #지역변수 : 함수 바깥에서 사용 x


def fun2():
    print("fun2()의 a =", a)

# fun2() #오류. 전역변수가 선언되기 전에 전역변수를 사용하는 함수가 호출됨

fun1() #지역 변수의 우선순위가 더 높음
fun2()


def fun3():
    global b
    b = 100
    print("fun3()의 변수 b :", b)


def fun4():
    print("fun4()의 변수 b :", b)

fun3()
fun4()

def calc_area(radius):
    global area
    area = 3.14*radius**2
    return area

# print(area) # 정의되지 않음 오류 남
print(calc_area(5))
print(area)