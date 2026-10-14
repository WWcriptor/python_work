# 사칙연산 return없이

def plus(x,y):
    print(f"{x}+{y}={x+y}")

def minus(x,y):
    print(f"{x}-{y}={x-y}")

def multi(x,y):
    print(f"{x}*{y}={x*y}")

plus(3, 8)
minus(8,3)
multi(2,3)

def plusRe(i, j):
    return i+j

def minusRe(i,j):
    return i-j

def multiRe(i,j):
    return i*j

result = plusRe(3,8)
print(result)
print(minusRe(result,7))
print(multiRe(4.56, 2.76))