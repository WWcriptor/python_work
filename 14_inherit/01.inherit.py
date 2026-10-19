class CalcParent:
    def plus(self, x, y):
        print("부모 클래스의 plus()")
        return x+y

    def minus(self, x, y):
        print("부모 클래스의 minus()")
        return x-y


class Calcchild(CalcParent): #매개변수에 부모의 클래스명 넣기 == 상속받기
    def multi(self, x, y):
        print("자식 클래스의 multi()")
        return x*y

    def plus(self, x, y):
        print("부모의 plus :", super().plus(x,y))
        print("자식 클래스의 plus()")
        return (x+y)*2


cal1 = Calcchild()
print(cal1.minus(5,3))
print(cal1.plus(3,1))

cal2 = CalcParent()
print(cal2.plus(3,5))
# print(cal2.multi(3,5)) #부모 클래스는 자식 클래스의 메서드를 사용 불가능