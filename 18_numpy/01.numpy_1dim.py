"""
    numpy
        python에서 배열과 행렬 같은 수치 데이터를 효율적으로 처리하고,
        다양한 수학, 통계, 계산 등을 수행하기 위한 라이브러리.

        - 장점 : N-dimensional array 다차원 배열을 다룸
"""

import numpy as np

data1 = [1,2,3,4,5]
data2 = [1.7, 2, 5.5, 8]
data3 = [1.7, 2, "5.5", 8.8]

# array() : 리스트나 튜플을 넘파이 배열로 만들어줌
arr1 = np.array(data1)
print(f"데이터 : {arr1}")
print(f"자료형 : {type(arr1)}")
print(f"데이터의 종류 : {arr1.dtype}")
print(f"배열의 구조 : {arr1.shape}")

# 배열으 특징 : 단일 데이터만 취급
# 정수와 실수가 섞여있을 경우 모두 실수로 변환하여 저장
arr2 = np.array(data2)
print(f"데이터 : {arr2}")
print(f"데이터의 종류 : {arr2.dtype}")
print(f"배열의 구조 : {arr2.shape}")

#정수, 실수, 문자열이 섞여있을 경우 모두 문자열로 변환하여 저장
arr3 = np.array(data3)
print(f"데이터 : {arr3}")
print(f"데이터의 종류 : {arr3.dtype}")
print(f"배열의 구조 : {arr3.shape}")