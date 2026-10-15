#가변 키워드 인자
#**kwarges : dictionary가 전달 됨

def print_info(**kwarges):
    for key, value in kwarges.items():
        print(key, ":", value)

print_info(name="홍길동")
print_info(name = "김미영", age = "35", city = "seoul")

#dictionalry를 넘겨줘도 됨
info = {"name":"이사랑", "age" : "23", "city":"Gyeongido"}

# print_info(info) #그냥 넘기면 에러. info라는 딕셔너리 객체 단1개 전달
print_info(**info) #**로 언패킹 필수