"""
    set: 중복불가,
         순서가 없다 = index가 없다
         {} 사용

         *** 주의 : 빈 set을 만들 때 set()으로 작성
                    ({}는 빈 딕셔너리로 읽음)
"""

a = {1,1,2,4,6,3,2,1,7,3,5,2,1,7}
print(a)
print(len(a))

b = {"홍길동", 5, True,(4,5), 3.14}
print(b)

c = {}
print(type(c))

d = set()
print(type(d))