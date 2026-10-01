# 변수 : 어떤 자료형이든 상관 없이 넣을 수 있음
v = "Hello Python"
#print(v)

#print(id(v)) #객체 주소를 출력하는 내장함수

v = 100
#print(id(v)) #값이 변할 경우 객체 주소가 바뀌는 원리

#변수 명 지정
#변수가 무엇을 가리키는 지 알 수 있는 이름으로 작명
#예약어(print, import 등등)는 변수명으로 사용 불가

#python의 자료 크기는 상관 x
num1 = 100
num2 = 1238490570198427490124891750184
num3 = 453.23424134820582
c = "흠"
s = "Hello world!!"
b = True

print(num1)
print(num2)
print(num3)
print(c)
print(s)
print(b)

print("-"*20)

print(f"num1's type : {type(num1)}")
print(f"num2's type : {type(num2)}")
print(f"num3's type : {type(num3)}")
print(f"c's type : {type(c)}")
print(f"s's type : {type(s)}")
print(f"b's type : {type(b)}")

print("-"*20)

a = 1
b = 2
c = 3

d, e, f = 1, 2, 3
print(d, e, f)

g, h, i = "더조은", False, 3.141592 #자료형이 다른 상태로 한 번에 넣는건 python에서만 가능
print(g, h, i)