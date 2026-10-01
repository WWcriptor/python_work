str1 =  "abcdefghijk"
print(str1[0])
print(str1[2])

print("-"*20)

#음수는 뒤에서부터 시작(-1 = 끝 인덱스)
print(str1[-1])
print(str1[-4])

print("-"*20)

#slicing
#[시작:끝:step] : step 생략 시 기본값 1
#끝 포함 X

print(str1[1:4])
print(str1[:3]) # == [0:3]
print(str1[2:]) # 이떄에는 끝 수도 포함
print(str1[:]) # == print(str)

print(str1[1:9:2])
print(str1[1:9:3])
print(str1[::2])
print(str1[::-3])
print(str1[5:1:-1])
print(str1[-1:-6:-1])

print("-"*20)

# 문자열 연결하기:+
str2 = "xyz"
str3 = str1 + str2
print(str3)

#문자열 반복 : *
str4 = str2 *3
print(str4)

#문자열의 개수 확인
print(len(str1))

print("-"*20)

#문자열은 인덱식으로 문자열을 부분적으로 변경 X
#str1[0] = "z" #오류
str1 = "z" + str1[1:] # 이런식으로는 활용 가능
print(str1)