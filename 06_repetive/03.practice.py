"""
    1~100까지의 합계를 구하기
    조건 : 사용자가 넣은 숫자의 배수만 합계 구하기
"""

start = int(input("시작값: "))
end = int(input("끝나는 값: "))
num = int(input("배수를 입력하세요: "))
sum = 0
count = 0


for i in range(start, end+1):
    if i % num == 0:
        sum += i
        count +=1
        if i<end+1-num:
            print(f"{i} +", end=" ")
        else:
            print(i)

print(f"{start}부터 {end}까지 {num}의 배수는 {count}개 이고, 합계는 {sum}입니다.")
