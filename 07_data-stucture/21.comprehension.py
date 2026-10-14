# Comprehension
# for문이나 if문으 한 줄로 넣는 방법을 의미
# 특히 리스트에서 많이 사용 -> list comprehension 으로 불림

result = [0,0,0,0,0,0,0,0,0,0]      #둘이
result = [0 for i in range(10)]     #같은 의미
print(result)

result = [10 for i in range(10)]
print(result)

result = [i+1 for i in range(100)]
print(result)

result = ["티알" for i in range(10)]
print(result)

data = [3, 5, 7, 9]
result = [i**2 for i in data]
print(result)

"""
num_list = [int(input("숫자 입력: ")) for i in range(5)]
print(num_list)
print(f"합계는 {sum(num_list)}입니다")
"""

# if와 for문이 함께 들어 있을 때 무조건 for문부터
# <explression> for 변수 in <iterable>
# if만 있는 경우 if문이 for문 뒤에, if와 else가 있는 경우 for문 앞에 if문 작성

result = []
for num in range(1,20):
    if num % 2 ==0:
        result.append(num*3)

result =[num*3 for num in range(1,20) if num % 2 == 0]
print(result)

result =[]
for num in range(1,10):
    if num % 2 ==0:
        result.append(num)
    else:
        result.append(0)

result = [num if num % 2 == 0 else 0 for num in range(1,10)]
print(result)

result = ["짝수" if num %2 ==0 else "홀수" for num in range(1,6)]
print(result)

# for문 중첩
result = []
for i in [1,2,3]:
    for j in [10, 20]:
        result.append((i,j))

result = [(i, j) for i in [1,2,3] for j in [10, 20]]
print(result)

result = []
for i in range(1,4):
    for j in range(1,4):
        if (i+j) % 2 ==0:
            result.append((i,j))


result = [(i,j) for i in range(1,4) for j in range(1,4) if (i+j) % 2 == 0]
print(result)

result = []
for i in range(1,4):
    for j in range(1,4):
        if (i+j) % 2 ==0:
            result.append((i,j))
        else:
            result.append((0,0))

result = [(i,j) if (i+j) % 2 == 0 else (0,0) for i in range(1,4) for j in range(1,4)]
print(result)

# unpacking
lst = [(1,11), (2,21), (3,31)]
for (i, j) in lst:
    s = i+j
    print(s)


print([i+j for (i, j) in lst])


#enumerat() : 인덱스 번호와 데이터를 tuple의 형태로 반환
t = [1,5,3,2,77,3,45]
for p in enumerate(t):
    print(p)

print("-"*20)

for index, value in enumerate(t):
    print(f"index: {index}, value: {value}")


# zip() : 리스트들을 동일한 위치값으로 묶어서 tuple로 반환
# 길이가 다를 경우 짧은 길이를 기준으로 함
list1 = [10,20,30]
list2 = [100,200,300]

for z in zip(list1, list2):
    print(z)

for a, b in zip(list1, list2):
    print(a+b)