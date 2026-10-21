# 범위를 지정하여 numpy배열 생성
# arange(start, end, step) / end 포함 안 함
import numpy as np

arr1 = np.arange(0,10,2)
print(f"데이터 : {arr1}")
print(f"배열의 구조 : {arr1.shape}")
print("-"*30)

arr2 = np.arange(1,10)
print(f"데이터 : {arr2}")
print(f"배열의 구조 : {arr2.shape}")
print("-"*30)

arr3 = np.arange(5)
print(f"데이터 : {arr3}")
print(f"배열의 구조 : {arr3.shape}")
print("-"*30)