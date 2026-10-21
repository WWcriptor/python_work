"""
    1. 1차원 배열 만들기
        numpy를 사용하여 1차원 배열 생성
        [10 20 30 40 50]

    2. 2차원 배열 만들기
        numpy를 사용하여 2차원 배열 생성
        [[1 2 3]
         [4 5 6]]

    3.arange()를 사용하여 5부터 20(20도 포함)까지 3씩 증가하는 1차원 배열을 생성

    4. arange()로 1부터 12까지의 숫자를 생성한 뒤, reshape()를 이용하여 3행 4열의 배열로 변환

    5. linspace()를 이용하여 0부터 1까지 동일한 간격으로 나누어진 숫자 6개를 생성

    6. 모든 원소가 0인 3행 4열의 배열 생성

    7. 모든 원소가 1인 2행 5열의 배열 생성. 단, 데이터 타입은 정수형으로

    8. 다음 조건을 만족하는 배열 생성
        - 2부터 24까지 짝수를 생성
        - 생성한 배열을 3행 4열로 변환한다

    9. 다음 조건을 만족하는 배열을 생성
        - 10부터 50까지 균등한 간격의숫자 9개를 생성
        - 생성한 배열을 3행 3열로 변환

    10 다음 세 가지 배열을 각각 생성
        1. arange()와 reshape()를 사용해 1부터 16까지의 숫자를 4행 4열로 만든다
        2. 모든 원소가 0인 4행 4열을 마든다
        3. 모든 원소가 1인 4행 4열의 정수형 배열을 만든다.

    11. 4행 4열의 단위 행렬읠 생성 (자료형 int)

    12. 3행 5열의 배열에서 주 대각선보다 한 칸 오른쪽에 1이 위치하도록 만들기
        자료형은 정수형으로 지정
"""
import numpy as np


# 1.
print(np.array([10,20,30,40,50]))
print(np.arange(10,51,10))
print("-"*30)

# 2.
arr1 = [1,2,3]
arr2 = [4,5,6]
print(np.array([arr1, arr2]))
print("-"*30)

# 3.
print(np.arange(5,21,3))
print("-"*30)

# 4.
arr3 = np.arange(1,13)
print(arr3.reshape(3,4))
print()
print(np.arange(1,13).reshape(3,4))
print("-"*30)

# 5.
print(np.linspace(0,1,6))
print("-"*30)

# 6.
print(np.zeros((3,4)))
print("-"*30)

# 7.
print(np.ones((2,5), dtype=int))
print("-"*30)

# 8.
arr4 = np.arange(2,25,2)
print(arr4.reshape(3,4))
print("-"*30)

# 9.
arr5 = np.linspace(10,50,9)
print(arr5.reshape(3,3))
print("-"*30)

# 10.
arr6 = np.arange(1,17)
print(arr6.reshape(4,4))
print()
print(np.zeros((4,4)))
print()
print(np.ones((4,4), dtype=int))
print("-"*30)

# 11.
print(np.eye(4, dtype=int))
print("-"*30)

# 12.
print(np.eye(3,5,k=1,dtype=int))