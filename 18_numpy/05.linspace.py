import numpy as np

#linspace(start, end, 개수)
# => 범위의 시작과 끝을 지정하고 개수를 넣으면 균등하게 등분(end 포함)

arr1 = np.linspace(1,5,100)
print(f"데이터 : {arr1}")
print(f"배열 구조 : {arr1.shape}")
print("-"*30)

arr2 = np.linspace(-1, 1, 10)
print(f"데이터 : {arr2}")
print(f"배열 구조 : {arr2.shape}")
print("-"*30)