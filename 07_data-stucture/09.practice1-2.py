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
"""
#초기 데이터 설정
student =[
    ["홍길동", 89,92,79,100], ["아무개", 73, 84, 96, 76], ["이순신", 92, 84, 72, 99]
]
sub_sum = [0,0,0,0]

print("과정\t파이썬\tAI\t빅데이터\t디자인\t합계\t평균")
for row in student:
    name = row[0]
    scores = row[1:]
    for i in range(4):
        sub_sum[i] += scores[i]
    
    
    student_sum = sum(scores)
    student_avg = student_sum/len(scores)

    #학생별 합계
    print(f"{name}\t{scores[0]}\t{scores[1]}\t{scores[2]}\t\t{scores[3]}\t{student_sum}\t{student_avg}")
print("-"*50)

sub_avg = [i / len(student) for i in sub_sum]

print(f"합계\t{sub_sum[0]}\t{sub_sum[1]}\t{sub_sum[2]}\t\t{sub_sum[3]}")
print(f"평균\t{sub_avg[0]:.1f}\t{sub_avg[1]:.1f}\t{sub_avg[2]:.1f}\t\t{sub_avg[3]:.1f}")
"""

name = ["홍길동", "아무개", "이순신"]
subjects = ["파이썬", "AI", "빅데이터", "디자인"]
score = [
    [89,92,79,100],
    [73, 84, 96, 76],
    [92, 84, 72, 99]
]

print("과정", end="\t")
for i in subjects:
    print(i, end="\t")
print("합계","평균", sep="\t")
for i in range(len(name)):
    total = sum(score[i])
    avg = total/len(subjects)

    print(f"{name[i]}\t{score[i][0]}\t{score[i][1]}\t{score[i][2]}\t{score[i][3]}\t{total}\t{avg:.1f}")

print("-"*50)

#과목별
print("합계", end="\t")
for j in range(len(subjects)):
    total = 0
    for i in range(len(name)):
        total += score[i][j]
    print(total, end="\t")
print()

#평균
print("평균", end="\t")
for j in range(len(subjects)):
    total = 0
    for i in range(len(name)):
        total += score[i][j]
    print(f"{total/len(name):.1f}", end="\t")