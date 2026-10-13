str_list = ["국어", "영어", "수학", "과학", "사회"]

print(str_list.index("영어"))
# print(str_list.index("Python")) #오류남

a = "파이썬"

if a in str_list:
    print(str_list.index(a))
else:
    print("데이터 없음")

print("-"*20)

#항목 추가 : 제일 뒤에 데이터 추가

str_list.append("Python")
print(str_list)

#데이터 중간에 삽입
str_list.insert(2,"인공지능")
print(str_list)

print("-"*20)

#데이터 정렬
#sorted : 데이터 원본을 바꾸지 않음
print(sorted(str_list)) #오름차순
print(sorted(str_list, reverse=True))
print(str_list)

print("-"*20)

#sort : 데이터 원본이 바뀜
str_list.sort()
print(str_list)

str_list.sort(reverse=True)
print(str_list)

print("-"*20)

#데이터 삭제. 없는 데이터를 넣으면 error
if "국어" in str_list:
    str_list.remove("국어")
print(str_list)

#모든 데이터 삭제
str_list.clear()
print(str_list)