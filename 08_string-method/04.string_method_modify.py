str1 =  "He likes apples, and she does, too"

# 특정 문자 기준으로 문자열을 분리
# 기본값 : 공백
# 결과값(반환값) : 리스트

str2 = str1.split()
print(str1)
print(str2)

print("-"*20)

# ,를 기준으로 분리
str2 = str1.split(",")
print(str2)

# 공백을 기준으로 3번만 분리. 리스트 개수는 n+1 (잘린 횟수 +1)
str2 = str1.split(" ", 3)
print(str2)

str2 = str1.split()
str3 = ",".join(str2) # 도로 붙이는 거
print(str2)
print(str3)