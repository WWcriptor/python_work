#continue 아래는 실행하지 않고 반복문으로 다시 올라감

x = 1
while True:
    print(x)
    x+=1

    if x == 6:
        x += 2
        continue
    if x == 10:
        break


#1~100까지 4의 배수를 제외하고 합산

sum = 0

for i in range(1,101):
    if i % 4 == 0:
        continue
    sum += i

print(sum)
