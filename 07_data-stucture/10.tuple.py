#tuple : 리스트와 동일하지만 변경 불가
#소괄호() -> 안 써도 됨

tup1 = (10,20,30,40)
tup2 = ("python", 4.78, 90, True)
tup3 = "python", 4.78, 90, True

# 데이터가 1개일 때
tup4 = (10,) #끝에 콤마를 찍어줘야 함
tup5 = 10,
tup6 = (10)

print(type(tup4))
print(type(tup5))
print(type(tup6))
print("-"*20)

print(tup1[1])
print(tup3[3])
print("-"*20)

# tup1[1]=100 #튜플은 값 변경 불가 -> 오류남

#변수 자체를 삭제
del(tup1)
# print(tup1) -> 오류남. 변수 자체가 삭제되었기 때문