#디폴트 매개변수

def greet(name, msg="안녕하세요"):
    print(f"{name}님 {msg}")

greet("홍길동")


def greet2(name, age, class1="704", aa="0000"):
    print(f"{name}님은 {age}세 이고, {class1}호실을 사용하며, id는 {aa}입니다")

greet2("홍길동", 34)
greet2("고길동", 34, "701", "3490")

#가변객체 사용 불가

def welcom(city, name="Guest", room =[]):
    room.append(101)
    print(f"Hello {name}, This is {city}. You can use {room}")

welcom("seoul")
welcom("seoul", "더조은")

def welcom2(city, name="Guest", room =None):
    if room == None:
        room = "101"
    print(f"Hello {name}, This is {city}. You can use {room}")

welcom2("seoul")
welcom2("seoul", "더조은", "1001")