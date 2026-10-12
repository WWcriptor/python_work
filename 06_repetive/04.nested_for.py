for i in range(3):
    for j in range(2):
        print(f"i:{i}, j:{j}")
print("-"*20)

for dan in range(2,10):
    print(f" {dan}단")
    for num in range(1,10):
        print(f"{dan}*{num}={dan*num}")
    print()


"""
    구구단 가로
    2*1=2 3*1=3 ........
    2*2=4 3*2=6
"""

for i in range(1,10):
    for j in range(2,10):
        print(f"{j}*{i}={j*i:2d}", end=" ")
    print()