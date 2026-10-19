class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    pass


d = D()
d.method()
# MRO(Method Resolution Order) 규칙: 다중 상속시 메서드를 찾는 순서
print(D.mro())