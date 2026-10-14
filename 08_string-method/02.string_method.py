str1 =  "He likes apples, and she does, too likes"

#문자열에서 특정 문자열의 개수 구하기
print(str1.count("like"))

# 왼쪽에서 오른쪽으로 문자열을 검색
p = str1.find("like")
print(p)
print(str1.find("like", p+1)) #그 다음 것
print(str1.find("banana"))

print("-"*20)

#오른쪽에서 왼쪽으로 문자열 검색
p = str1.rfind("like")
print(p)
print(str1.rfind("like",0, 3))

# index() : find()와 기능은 같지만 없으면 예외 발생
p = str1.index("like")
print(p)
# print(str1.index("banana")) #ValueError 발생

# 시작하는 단어인지 검사
print(str1.startswith("like"))
print(str1.startswith("like", 3))

# 끝나는 단어인지 검사
print(str1.endswith("like",0,-1))