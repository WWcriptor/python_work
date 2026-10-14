# return에 값이 2개 이상이면 자동으로 튜플로 반환

def tm(x,y):
    sum = x+y
    mul = x*y

    return sum, mul

result = tm(5,10)
print(result, type(result))

print(f"합은 {result[0]}, 곱은 {result[1]}입니다")

total, multi = tm(5,10)
print(f"합은 {total}, 곱은 {multi}입니다")