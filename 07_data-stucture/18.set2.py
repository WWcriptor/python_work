s ={1,2,3,1,2,3,4,1,5,3,5}

print(2 in s)
print(6 in s)

#데이터 추가
s.add(10)
print(s)

#update 가능
s.update({5,11,12,15})
print(s)

#개별 삭제 가능
s.remove(1)
print(s)

#전체 삭제
s.clear()
print(s)