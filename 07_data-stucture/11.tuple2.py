str_tup = ("국어","영어","수학","파이썬","AI")

print(str_tup[::2])
print(str_tup[::-1])

print(str_tup.index("국어"))

tup1 = (1,2,3,4,5)
print("%d %d %d %d" %(tup1[0], tup1[4], tup1[2], tup1[1]))
print(f"{tup1[0]} {tup1[4]}")
print("{0}{3}{1}{2}" .format(tup1[0],tup1[1],tup1[2],tup1[3]))

#언패킹 : 튜플의 포장을 풀어서 안의 내용만 출력
# *변수명
print("{}{}{}".format(*tup1))
print("{}{}{}".format(*tup1[-3:]))
print(*tup1[:3])
print(tup1[:3]) #언패킹을 하지 않을 경우 튜플의 형태로 반환

tup2 = (34.2523, 9.259, 45.3902, 8.3324)
print("{:.2f} {:.2f} {:.2f} {:.2f}" .format(*tup2))

for i in range(len(tup2)):
    if i < len(tup2)-1:
        print("{:.2f}".format(tup2[i]), end=", ")
    else:
        print("{:.2f}".format(tup2[i]))

#join() : 열러개의 문자열을 하나로 합칠 때 사용하는 문자열 메서드(함수)

            # 구분자 join(문자열이 담긴 리스트나 튜플)

words = ["python", "is", "fucn"]
#공백을 기준으로 합치기
print(" ".join(words))

#하이픈을 기준으로 합치기
print("-".join(words))

#for문을 한줄로 작성
print(", ".join(f"{i:.2f}" for i in tup2))


tup3 = (10, 20, 30)
a, b, c = tup3
print(a, b, c)

d, e = tup3[:2]
print(d, e)