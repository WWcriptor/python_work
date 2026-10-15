student =[]
student2 =[]
with open("test.csv", "r", encoding="UTF-8")as f:
    #lines = f.read().splitlines()
    lines = f.readlines()
    # print(lines)

    for line in lines:
        #line = line.strip()
        # print(line)
        line = line.split(",")
        # print(line)
        student.append(line)

    #줄여쓸 수 있음
    for line in lines:
        student2.append(line.strip().split(","))

    student3= [line.strip().split(",") for line in lines]

with open("test.csv", "r", encoding="UTF-8")as f:
    student4= [line.split(",") for line in f.read().splitlines()]


print(student)
print(student2)
print(student3)
print(student4)

for i in student4:
    name = i[0]
    kr = int(i[1])
    ma = int(i[2])
    en = int(i[3])
    total = kr + ma + en
    avg = total/3
    print(f"이름: {name}, 국어: {kr}, 수학: {ma}, 영어: {en}, 총점: {total}, 평균: {avg:.2f}")

print("-"*50)

result =""
for i in student4:
    name, kr, ma, en = i
    total = int(kr) + int(ma) + int(en)
    avg = total/3
    result += f"이름: {name}, 국어: {kr}, 수학: {ma}, 영어: {en}, 총점: {total}, 평균: {avg:.2f}\n"
print(result)

with open("result.txt", "w", encoding="UTF-8")as r:
    r.write(result)