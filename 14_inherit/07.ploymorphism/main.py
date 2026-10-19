"""
추상 클래스
    : 추상 메소드가 포함되어 있는 클래스
        > 추상 메소드 : 구현하지 않은 메소드
    - 추상 클래스를 상속받는 클래스는 반드시 추상메소드를 구현해야 한다.
    - 추상 클래스는 객체를 생성할 수 없다

추상 클래스를 만드는 방법
    - abc : Abstract Base Class(추상 기본 클래스)의 약자
            파이썬에서 추상 클래스를 정의할 때 사용하는 내장모듈
    - ABC : abc 모듈에 들어있는 클래스
    - abstractmethod : 추상 메소드 위에 @bstractmethod 어노트에션을 달아야 한다.
    - 추상크래스는 import를 반드시 해야 한다.
        from abc import ABC, abstractmethod

    - 본 클래스에서는 ABC 클래스를 상속받아야 한다.
        class Kim(ABC):
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