import numpy as np

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.arange(10, 100, 10).reshape(3,3)

print(f"arr1 : {arr1}")
print(f"arr2 : \n{arr2}")
print("-"*30)

# 1차원 배열의 슬라이싱
print(arr1[1:4])
print(arr1[:4])
print(arr1[1:])
print(arr1[::2])

arr1[1:4] = [100,200,300]
print(f"arr1 : {arr1}")
print("-"*30)

# 2차원 배열의 슬라이싱
# 배열명[행 슬라이싱, 열 슬라이싱]
# 배열명[:2,1:3]
print(f"arr2 : \n{arr2}")
print(arr2[0:2,1:3])

print(arr2[:2, :2])

# 특정 열만 추출
print(arr2[1][0:2])
print(arr2[:,2])
print(arr2[:,[1,2]])
print("-"*30)

#특정 행만 추출
print(arr2[1, :])
print(arr2[[1,2],:])