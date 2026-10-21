#정방행렬 : 행과 열의 수가 같은 n*n 형식의 행렬
#단위행렬 : 정방행렬 중에서 대각선만 1이고 나머지가 0인 행렬

import numpy as np

#단위행렬(대각선 위치 못 바꿈)
print(np.identity(5))
print("-"*30)

#직사각 행렬
# eye(N, M=None, K=0, dtype = float)함수 
# N은 행(필수), M은 열(넣지 않으면 정방행렬 생성), K는 1을 채울 대각선 위치, dtype은 데이터 타입 

#3*3 단위행렬 생성
arr1 = np.eye(3)
print(arr1)
print(f"베열 구조 : {arr1.shape}")
print("-"*30)

# 2*4
arr2 = np.eye(2,4)
print(arr2)
print(f"베열 구조 : {arr2.shape}")
print("-"*30)

# 대각선의 위치 변경
print(np.eye(5, k=1)) # k가 양수이면 위로 n만큼
print("-"*30)
print(np.eye(5, k=-1)) # k가 음수이면 아래로 n만큼
print("-"*30)
print(np.eye(4,5,2))
print("-"*30)
arr3 = np.eye(3, dtype=int)
print(arr3)
