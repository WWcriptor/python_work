import numpy as np

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.arange(10, 100, 10).reshape(3,3)

print(f"arr1 : {arr1}")
print(f"arr2 : {arr2}")
print("-"*30)

# 1차원 배열의 인덱싱
print(arr1[0])
print(arr1[[1,3,5]]) #[20 40 60]
print(arr1[arr1>30]) #[40 50 60]

arr1[2] = 555
print(f"arr1 : {arr1}")

arr1[[1,3,5]] =[333,777,999]
print(f"arr1 : {arr1}")

arr1[arr1>30] = 0
print(f"arr1 : {arr1}")

# 2차원 배열의 인덱싱
print(f"arr2 : \n{arr2}")
print(arr2[0,2]) #이 표현식을 권장
print(arr2[0][2])

arr2[0,2] =1000
print(f"arr2 : \n{arr2}")


#행을 통째로 변경
arr2[1] = [1,2,3]
print(f"arr2 : \n{arr2}")

print(arr2[[0,2], [1,1]]) #[[행, 행], [열, 열]]
arr2[[0,2], [1,1]] =[100,200]
print(f"arr2 : \n{arr2}")