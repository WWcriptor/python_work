"""
    Q1. 삼각형의 넓이를 구하는 파일(class) 생성
        실행하는 파일 만들어 import 해서 실행한 결과 출력

    Q2. 별도의 클래스에 메서드 2개 만들기
        메서드 1 : 이름, 파이썬 점수, AI점수를 사용자로부터 입력받기
        메서드2 : 출력문
            출력문 ex)
            이름 : 김수영
            파이썬 : 98
            AI : 79
            합계 : 177
            평균 : 87.7
        실행파일 " 2명으로부터 입력받아 2명 출력하기


"""
from prac01 import Area

num1 = int(input("삼각형의 밑변 길이 : "))
num2 = int(input("삼각형의 높이 : "))

tri = Area()
result = tri.calc_area(num1, num2)

print(result)

print("-"*30)

from prac01 import Score

student1 = Score()
student2 = Score()

student1.put_info()
student2.put_info()

print("-"*30)

student1.out_info()
student2.out_info()
