# 함수명 = lambda 매개변수 : 수행코드


square1 = lambda x : x**2

print(square1(10))

""" 일반 함수 표현식
def square1(x):
    return x**2
"""

test1 = lambda : print("test1")

test1()

a = (lambda x : x**2)(3)
print(a)
print((lambda x : x**2)(3))

(lambda : print("test2"))() # 뒤의 괄호는 앞의 함수를 지금 실행하라라는 의미의 명령어


list1 = [(lambda x, y, z : x+ 2*y + z**2)(1,2,3)]
print(list1)

print((lambda x, y, z : x+ 2*y + z**2)(1,2,3))

print([(lambda x : x**2)(a) for a in range(1,6)])