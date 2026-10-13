dic1 = {"a":1,  "c":"hello", "b":3.141592, "d":"Python"}

#key가 없을 경우 대비
if "e" in dic1:
    print("키가 존재합니다.", dic1["e"])
else:
    dic1["e"] = "bye"
print(dic1)

#key만 확인
keys = dic1.keys()
print(keys)
print(type(keys))

values = dic1.values()
print(values)
print(type(values))

#items() : 딕셔너리의 키와 값을 쌍으로 묶어서 가져오는 함수
print(dic1.items())

for key in dic1.keys():
    print(key)

print("-"*20)

for key, value in dic1.items():
    print(key, value)

print("-"*20)

for key in sorted(dic1.keys(), reverse=True):
    print(key, dic1[key])

print("-"*20)

dic1 = {"a":1, "b":3, "c":2, "d":5}

#값을 기준으로 오름차순 정렬
for value in sorted(dic1.values()):
    print(value)

print("-"*20)

#길이
print(len(dic1))

#데이터 추가
dic2 = {"e" : "Python", "f":"deepleaning"}
# dic1["g"] = dic2
# print(dic1) #{'a': 1, 'b': 3, 'c': 2, 'd': 5, 'g': {'e': 'Python', 'f': 'deepleaning'}}

dic1.update(dic2)
print(dic1) #{'a': 1, 'b': 3, 'c': 2, 'd': 5, 'e': 'Python', 'f': 'deepleaning'}