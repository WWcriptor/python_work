"""
    import 모듈명
        -> 모듈명.명령어
    from 모듈명 import 함수, 클래스명
"""
import random
print(random.__file__)

from random import random
from random import randint
from random import randrange
from random import sample

print(random())
print(randint(0,9))
print(randrange(5,10,2)) #step을 줄 수 있음

# 아스키코드 A(65)~Z(90),  a(97)~z(122)

print(chr(randint(65, 90)))


#리스트에서 개수를 선택하여 임의의 값 추출
list1 =[435,24,52,73,35,83,36]
print(sample(list1, 2))
print(sample([i for i in range(1,46)], 6))