str1 =  "He likes apples, and she does, too"

#가운데 정렬
str2 = str1.center(50)
print(str1)
print(str2 + "끝")

#공백 대신 '-' 채우기
str2 = str1.center(50, "-")
print(str2)

#오른쪽 맞춤
str2 = str1.rjust(50)
print(str2)

#왼쪽 맞춤
str2 = str1.ljust(50)
print(str2+"끝")

str3 = "1\tand\t2"
print(str3)
str4 = str3.expandtabs(10) #비울 시 기본 값은 8(그냥 탭하고 같음)
print(str4)