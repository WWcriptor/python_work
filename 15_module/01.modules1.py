"""
    - 모듈 : 파이썬 코드가 저장된 하나의 파일
            관련된 변수, 함수, 클래스... 모두 넣을 수 있음
    - 클래스: 변수, 메서드를 넣을 수 있음. 객체를 생성해서 사용

    - 비교 : 
            구분       | 모듈(Module)                          | 클래스(class)
            ------------------------------------------------------------------------------------
            정의 기준     | 하나의 파일(.py)                       |   파일 내부의 코드블록(class...)
            인스턴스화    | 불가능(자체로 사용)                     | 가능
            주요 목적     | 관련함수/변수를 파일 단위로 정리, 재사용 | 데이터와 기능을 묶어 여러 개체 
            객체지향 가능 | 상속, 다형성 등 사용 불가            | 상속, 다형성, 캡슐화 사용 가능
"""

# 모듈 사용법 1
# import 모듈명(=파일명)

import my_module1
my_module1.my_func()

# 모듈 사용법 2
# import 모듈명 as 별칭

import my_module1 as my
my.my_func()

# 모듈 사용법 3
# from 모듈명 import 함수명

from my_module1 import my_func
my_func()

# 모듈 사용법 4
# from 모듈명 import 함수명 as 별칭

from my_module1 import my_func as mf
mf()