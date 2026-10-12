# 1~100까지 합계 구하기
sum = 0

for i in range(1,101):
    sum += i
print(sum)

#1~100까지 5의 배수의 합 구하기

sum = 0

for i in range(1,101):
    if i % 5 == 0:
        sum += i

print(f"1부터 100까지 5의 배수의 합은 {sum}입니다")

sum = 0

for i in range(0,101, 5):
    sum += i
print(f"1부터 100까지 5의 배수의 합은 {sum}입니다")