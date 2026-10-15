#가변 위치 인자 : 매개변수의 개수가 정해져 있지 않을 때 사용
# *args : 튜플이 전달되고 저장됨

def total(*args):
    print(type(args))
    sums = 0
    for i in args:
        sums += i
    return sums

print(total(1,3))
print(total(1,3, 30, 50,29, 394))
print(total())
print("-"*30)

#매개변수가 여러개 일떄

def add_mul(op, *args):
    if op == "add":
        result = 0
        for i in args:
            result += i
    elif op == "mul":
        result = 1
        for i in args:
            result *= i
    else:
        result = "연산자가 잘못 작성됐습니다."
    return result

print(add_mul("add", 1,4,6,2,3,7))
print(add_mul("mul", 5,53,6,2,7,4,23))

def calc_sum(name, *args, academy):
    print(f"Name: {name}, Academy : {academy}")
    sums = 0
    for i in args:
        sums += i
    return sums

print(calc_sum("최상급", 1,3,4,6,2, academy="더조은"))