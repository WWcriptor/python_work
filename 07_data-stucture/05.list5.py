list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)

print(list1)

list2 = [1, 2, 3]
list2.append(4)
list2.append(5)

print(list2)

#리스트[]로 append하면 중첩 형식
list3 = [1,2,3]
list3.append([4,5]) # 중첩 리스트
print(list3) #[1,2,3,[4,5]]

#리스트[]로 extend하면 1차원의 데이터 맨 뒤에 들어감
list4 = [1,2,3]
list4.extend([4,5]) #중첩이 아니라 리스트 목록으로 들어감
print(list4) #[1,2,3,4,5]

list5 =[]
for i in range(100):
    list5.append(i+1)

print(list5)