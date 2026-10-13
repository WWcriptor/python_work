#{key:value} 쌍으로 구성. 키는 유일해야 함.

dic1 = {"a":1, "b":3.141592, "c":"hello", "d":"Python"}
dic2 = {1:1, 2:3.141592, 3:"hello", 4:"Python"}
dic3 = {1.1:1, 2.1:3.141592, 3.1:"hello", 4.1:"Pyhon"}
print(dic1)
print(dic2)
print(dic3)

#개별 데이터의 값을 얻어올 때 '키'를 넣어줌
print(dic1["a"],dic1["c"])
print(dic2[4])
print(dic3[2.1])

#새로운 값 넣기. 키가 없으면 삽입, 키가 있으면 변경
dic1["더조은"] = "02-1234-5678"
print(dic1)

dic1["더조은"] = "강남"
print(dic1)

#데이터 개별 삭제
del(dic1["더조은"])
print(dic1)

#데이터 전체 삭제
dic1.clear()
print(dic1)