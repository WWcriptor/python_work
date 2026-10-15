"""
    Q1.카페 주문
    메뉴와 사이즈 2개를 입력받음.
    만약 사이즈가 입력이 안 되면 무조건 small 사이즈

    Q2.택배 배송 정보
    받는 사람, 주소, 전화번호를 입력받음.
    순서와 상관없이 받아서 출력

    Q3.친구들과 식당에 가서 각자 낸 금액의 합계 구하기(tuple)
    친구들이 갈 떄마다 인원이 달라짐

    Q4.회원가입 정보를 입력받기(dict)
    사람마다 입력하는 정보의 개수가 다를 수 있음
"""

def order(menu, size="small"):
    print(f"메뉴 : {menu}, 사이즈 : {size}")

order("초코프라페", "venti")
order("아메리카노")

def dilivery(name, address, phone):
    print(f"받는 사람 : {name}, 주소 : {address}, 전화번호 : {phone}")

dilivery(address="강남구 삼오빌딩", name="이춘팔", phone="010-1234-4535")

def total_price(*args):
    total = 0
    for i in args:
        total += i
    return total

print(total_price(10,4,25,74,73))

def sign_up(**kwarg):
    for key, value in kwarg.items():
        print(f"{key} : {value}")

sign_up(name= "이수찬", age = 30, address = "강남구 어쩌고", phone="010-4492-1483")