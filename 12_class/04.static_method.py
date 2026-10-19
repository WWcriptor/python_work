#클래스(static) 메소드
#공동으로 사용

"""
    self를 쓰지 않았을 때 
        - 정적메서드로 사용시 
            class Car:
                @staticmethod
                def 정의

        - 호출시
        클래스이름.메서드이름
        객체생성이름.메서드이름
"""

class Calc:
    @staticmethod #이걸 달아주면 인스턴스에서 static 메서드로 변함
    def plus1(x,y):
        print('static 메서드 호출')
        return x+y

    def plus(self, x, y):
        print('인스턴스 메서드 호출')
        return x+y

    def minus(self, x, y):
        return x-y

    def result(self, x, y):
        result1 = Calc.plus1(x,y)
        result2 = self.plus(x,y)
        return result1+result2

# print(Calc.plus1(100,50))

# cal1 = Calc()
# print(cal1.plus(1,2))
# print(cal1.plus1(5,5))

cal2 = Calc()
print(cal2.plus1(5,100)) 
# @staticmethod가 없으면 오류남. 
# 객체를 만들 경우 첫 번째 매개변수에 자동으로 self 할당, but plus1에는 self 없음
# -> 엥 왜 객체 3갠데 2개밖에 안 들어와? 오류.(이떄 비워진 값은 y)