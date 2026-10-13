kim = [100, 95, 60]
park = [89,53, 88]
lee = []

sums = [0,0,0]
# for i in kim:
#     sums[0] += i

sums[0] = sum(kim)
sums[1] = sum(park)

for i in range(3):
    lee.append(int(input("점수를 입력하세요: ")))
sums[2] = sum(lee)

print(f"kim의 점수 총 합은 {sums[0]}점, 평균은 {sums[0]/len(kim):.2f}점 입니다.")
print(f"park의 점수 총 합은 {sums[1]}점, 평균은 {sums[1]/len(park):.2f}점 입니다.")
print(f"lee의 점수 총 합은 {sums[2]}점, 평균은 {sums[2]/len(lee):.2f}점 입니다.")
