"""
identity 연산자
is : 변수의 주소값이 같은지 검사
    -> True : 주소가 같다
    -> False : 주소가 다르다
is not : 변수의 주소값이 다른지 검사
    -> True : 주소가 다르다
    -> False : 주소가 같다

id() : 주소값 확인시 사용
"""

a = 1
b = 2
c = 1
print(f"a의 주소 : {id(a)}")
print(f"b의 주소 : {id(b)}")
print(a is b)
print(f"c의 주소 : {id(c)}")
print(a is not c)

b = 1
print(f"b의 주소 : {id(b)}")
print(a is b)