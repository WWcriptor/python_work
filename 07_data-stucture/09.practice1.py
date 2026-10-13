"""
    2차원 리스트로
    과정    파이썬   AI   빅데이터   디자인  합계  평균
    홍길동    89     92     79      100
    아무개    73     84     96       76
    이순신     
    --------------------------------------------------
    합계
    평균
"""

#초기 데이터 설정
student =[
    ["홍길동", 89,92,79,100], ["아무개", 73, 84, 96, 76], ["이순신", 92, 84, 72, 99]
]

total = [0 for i in range(len(student))]

print("과정  파이썬  AI  빅데이터  디자인  합계  평균")
for i in range(len(student)):
    for j in range(len(student[i])):
        if type(student[i][j]) == str:
            print(student[i][j], end="    ")
        else:
            print(student[i][j], end="    ")
            total[i] += student[i][j]
    print(total[i], end="    ")
    print(total[i]/(len(student[i])-1))

print("-"*40)

total2 = []

for i in range(len(student[0])):
    total2.append(0)
    for j in range(len(student)):
        if type(student[j][i]) == int:
            total2[i] += student[j][i]

print("합계", end="    ")
for i in range(len(student[0])-1):
    print(f"{total2[i+1]:>4d}", end="  ")

print()
print("평균", end="    ")
for i in range(len(student[0])-1):
    print(f"{total2[i+1]/len(student):.1f}", end="  ")