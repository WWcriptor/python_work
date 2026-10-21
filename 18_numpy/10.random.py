from numpy import random
f1 = random.rand()
print(f1)

from numpy.random import randint, rand, randn
f1 = rand()
print(f1)

f2 = random.rand(10)
print(f2)

print("-"*30)

#2행 3열의 2차원 배령 생성
f3  = random.rand(2,3)
print(f3)

#3차원 배열 생성
f4 = random.rand(3,2,3)
print(f4)

# radint (low=0, high, size = 1)
# low <= 난수 < hign 정수배열 생성
# size : n차원

n1 = random.randint(10)
print(n1)
print("-"*30)

n2 = random. randint(1, 10, size=(5,))
print(n2)
print(n2.shape)
print("-"*30)

n3 = random.randint(1, 10, size=(2,3))
print(n3)
print(n3.shape)
print("-"*30)

#3차원 배열 1~9 3행 4열이 2개
n4 = random.randint(1,9,size=(2,3,4))
print(n4)
print(n4.shape)
print("-"*30)

# randn() : 표준정규분포 난수
weight = random.randn(2,3)
print(weight)