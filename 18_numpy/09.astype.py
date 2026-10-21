import numpy as np

data1 = ["people", "male", "female", "boy", "girl"]
data2 = ["1.5","3.3","9.2","12.6"]
data3 = ["10", "20", "30"," 40", "50"]

arr1 = np.array(data1)
arr2 = np.array(data2)
arr3 = np.array(data3)

print(f"arr1 : {arr1}")
print(f"arr2 : {arr2}")
print(f"arr3 : {arr3}")
print("-"*30)

#실수로 구성된 문자열을 실수형으로 변경
arr4 = arr2.astype(float)
print(f"arr4 : {arr4}")
print(f"arr4 type : {arr4.dtype}")
print("-"*30)

arr5 = arr3.astype(int)
print(f"arr5 : {arr5}")
print(f"arr5 type : {arr5.dtype}")
print("-"*30)

arr6 = arr5.astype(str)
print(f"arr6 : {arr6}")
print(f"arr6 type : {arr6.dtype}")
print("-"*30)