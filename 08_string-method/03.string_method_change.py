str1 =  "    He likes apples, likes and she does, likes too          "

#좌우 공백 제거
str2 = str1.strip()
print(str1 + "끝")
print(str2 + "끝")

print("-"*20)

#오른쪽 공백 제거
str2 = str1.rstrip()
print(str1 + "끝")
print(str2 + "끝")

#왼쪽 공백 제거
str2 = str1.lstrip()
print(str1 + "끝")
print(str2 + "끝")

print("-"*20)

#문자열 바꾸기
str2 = str1.replace("like", "love", 1) #(바꿀 원래 요소, 바꿀 요소, 횟수)
print(str1)
print(str2)

str3 = "hello"
print(str3.replace("h", "H"))

str2 = str1.replace(" ","")
print(str1)
print(str2)