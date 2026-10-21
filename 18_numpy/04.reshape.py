import numpy as np

arr1 = np.arange(1,13)
print(f"데이터 : {arr1}")
print(f"배열 구조 : {arr1.shape}")
print("-"*30)

#reshape : 배열의 차원 변경
#2차원 배열로 변경
arr2 = arr1.reshape(3,4)
print(f"데이터 : {arr2}")
print(f"배열 구조 : {arr2.shape}")
print("-"*30)

#reshape에서 -1은 고정된 열이나 행에 ㅏㅈ춰 알아서 잘 변형하라는 의미
arr3 = arr1.reshape(2, -1) #행에 맞춰 열 자동 계산
print(f"데이터 : {arr3}")
print(f"배열 구조 : {arr3.shape}")
print("-"*30)

arr4 = arr1.reshape(-1, 3) #열에 맞춰 행 자동 계산
print(f"데이터 : {arr4}")
print(f"배열 구조 : {arr4.shape}")
print("-"*30)

#3차원 배열로 변경
arr5 = arr1.reshape(2,2,3)
print(f"데이터 : {arr5}")
print(f"배열 구조 : {arr5.shape}")
print("-"*30)

arr6 = arr4.reshape(2,2,3)
print(f"데이터 : {arr6}")
print(f"배열 구조 : {arr6.shape}")
print("-"*30)

# 3차원 배열을 1차원 배열로 변경
arr7 = arr5.reshape(-1)
print(f"데이터 : {arr7}")
print(f"배열 구조 : {arr7.shape}")
print("-"*30)