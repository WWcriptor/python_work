"""
    파일명은 소문자로 시작, 클래스명은 대문자로 시작

    클래스 선언
        class 클래스명:
            메서드(함수) 생성 or pass 작성(임시 점유용 키워드. 빈 상태로 만들 때 사용)

    매개변수 self
        자기자신의 객체를 의미
        클래스 안에서 함수를 호출할 때

        이름이 반드시 self일 필요는 없음 but self를 많이 사용
"""

class Car:
    def set1(self):
        self.model = "sm7"
        self.color = "blue"
        self.speed = 10

    def speedUp(self):
        self.speed += 10

    def output(self):
        print(f"모델: {self.model}, 색상: {self.color}, 속도: {self.speed}")

car1 = Car()
car1.set1() #호출 할 떄 변수가 생성되며 초기화(없으면 다른 메서드 오류남)
car1.output()

print("-"*30)

car1.speedUp()
car1.output()

print(car1.model)
print(car1.color)
print(car1.speed)