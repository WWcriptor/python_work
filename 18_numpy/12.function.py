import numpy as np

arr1 = np.arange(10,61,10)
print(arr1)

print(f"합계 : {arr1.sum()}")
print(f"평균 : {arr1.mean()}")
print(f"분산 : {arr1.var()}")
print(f"표준편차 : {arr1.std()}")
print(f"최소값 : {arr1.min()}")
print(f"최대값 : {arr1.max()}")
print(f"누적합 : {arr1.cumsum()}")
print(f"누적곱 : {arr1.cumprod()}")
print("-"*30)

print(f"합계 : {np.sum(arr1)}")
print(f"평균 : {np.mean(arr1)}")
print(f"분산 : {np.var(arr1)}")

# 2차원 배열의 평균 구하기
arr2 = arr1.reshape(2,3)
print(f"arr2 :\n{arr2}")

print(f"전체평균 : {np.mean(arr2)}")
print(f"행의 평균 : {np.mean(arr2, axis=1)}") # axis =1 은 가로 연산
print(f"열의 평균 : {np.mean(arr2, axis=0)}") # axis =0 은 세로 연산

print(f"최소값 : {np.min(arr2)}")
print(f"행 최소값 : {np.min(arr2, axis=1)}")
print(f"열 최소값 : {np.min(arr2, axis=0)}")

#중앙값 : median() -> 정렬 후 중앙값 추출
#데이터가 홀수 일때는 중앙값
arr3 = np.array([1, 2, 100])
print(f"중앙값 : {np.median(arr3)}")

#데이터가 짝수일 때는 중앙값 두 개의 평균
arr4 = np.array([1,100,4,2])
print(f"짝수 개 중앙값 : {np.median(arr4)}")

#2차원 배열의 축별 중앙값
arr5 = np.arange(1,13).reshape(3,4)

print(arr5)

print(f"전체 중앙값 : {np.median(arr5)}")
print(f"행별 중앙값 : {np.median(arr5, axis=1)}")
print(f"열별 중앙값 : {np.median(arr5, axis=0)}")