sum = 0

for i in range(1,101):
    sum+=i

print(sum)

"""
    초기값
    while 조건식:
        증가값
"""

i=1
sum=0

while i<=100:
    sum += i
    i += 1
print(sum)

total =0
i =1

while True:
    if i > 100:
        break
    total += i
    i += 1
print(total)