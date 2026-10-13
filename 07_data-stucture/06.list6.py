"""
    사용자로부터 정수 4개를 입력받아
    리스트에 저장하고 합계를 출력
"""
#numsList =[0 for i in range(101)] #0이 100개 든 리스트 생성
nums =[]

for i in range(4):
    num = int(input("숫자를 입력하세요: "))
    nums.append(num)
sums = sum(nums)

print(f"{nums}의 합계는 {sums} 입니다.")


numList = [int(input("숫자 : ")) for i in range(4)]
total = sum(numList)

print(total)