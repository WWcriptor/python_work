#다른 클래스를 사용할 때
#1) import 파일명
#2) from 파일명 import 클래스명
 
#1)
# import calculator05

# cal1 = calculator05.Calculator()
# print(cal1.plus(10,20))
# print(cal1.mul(10,20))


#2)
# from calculator05 import Calculator

# cal2 = Calculator()
# print(cal2.plus(10,20))
# print(cal2.mul(10,20))

#3)
from calculator05 import Calculator as c

cal3 = c()

