"""
논리 연산자 : 수학의 boolean 대수 연산
<진리표>
x | y | x and y | x or y | not x | x ^ y(xor / 서로 다를 떄만 True)
T | T |    T    |   T    |   F   |   F
T | F |    F    |   T    |   F   |   T
F | T |    F    |   T    |   T   |   T
F | F |    F    |   F    |   T   |   F
"""


num1 = 100
num2 = 200
x = 7
y = 3

f_result = num1 >= num2 # False
t_result = x >= y # True

print(f"f_result = {f_result}, t_result = {t_result}")

and_result = f_result and t_result
or_result = f_result or t_result

print(f"f_result and t_result = {and_result}")
print(f"f_result or t_result = {or_result}")
print(f"not f_result = {not f_result}")
print(f_result ^ t_result)