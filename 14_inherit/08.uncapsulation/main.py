"""
1. 각 클래스의 모든 인스턴스 변수는 private으로 변경
2. 추상클래스를 제외한 모든 클래스에서 추상 클래스의 인스턴스 변수를 호출하여 출력하는 메소드 정의
3. main에서 출력
"""

from programmer import Programmer
from acter import Acter
from famer import Famer

# people = Programmer("김수철", 31, "python")
# people.introduce()
# print("-"*30)

# people = Acter("박수철", 29, "왕과 사는 남자")
# people.introduce()
# print("-"*30)

# people = Famer("이수철", 28, "당근")
# people.introduce()

people = [Programmer("김수철", 31, "python"),
          Acter("박수철", 29, "왕과 사는 남자"),
          Famer("이수철", 28, "당근")]

print("============= 자기소개 하기(다형성 활용) =============")

for person in people:
    person.introduce()
    print("-"*30)