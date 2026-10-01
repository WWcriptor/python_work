"""
소속 연산자
in : 어떤 데이터가 특정 데이터 안에 있는지 검사
    -> True : 있다
    -> False : 없다
not in : 어떤 데이터가 특정 데이터 않에 없는지 검사
    -> True : 없다
    -> False : 있다
"""

str = "abcdefg"
print('ab'in str)
print('xy'in str)
print('c d'in str)

print('ab'not in str)
print('xy'not in str)
print('c d'not in str)