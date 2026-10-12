for x in "abcdefg":
    print(x)

print("-"*20)

num = [0,5,2,6]
for i in num:
    print(i)

print("-"*20)

"""
    range(start, stop, step) => 1,6 : 1~5까지
    rage(stop) 값이 하나만 들어있을 땐 종료값. 시작값은 0
    range(start, stop) 
"""

for i in range(5):
    print(i)

print("-"*20)

for i in range(3,10):
    print(i)

print("-"*20)

for i in range(1, 10, 3):
    print(i)

print("-"*20)

for i in range(1, 20, 2):
    if i < 19:
        print(i, end=", ")
    else:
        print(i)
