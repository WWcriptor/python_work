"""
bool() 변환

False가 되는 경우
    : 완전히 비어있거나, 0인 경우(0, 0.0, ""(빈 문자열), None, [](빈 리스트))
데이터가 하나라도 들어있는 경우는 모두 True (" "(공백)도 데이터로 침)
"""

print(bool(6))
print(bool(0))

print("-"*20)

print(bool("집에 보내줘"))
print(bool(""))
print(bool(" "))

print("-"*20)

print(bool(3.14))
print(bool(0.0))

print("-"*20)
a = 5
b = None

print(bool(a))
print(bool(b))