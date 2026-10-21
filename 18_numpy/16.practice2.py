import numpy as np
#1. 다음 배열에서 정수형 배열을 생성하고, 변환된 배열의 자료형 및 원본 배열 출력
#a = np.array([1.8, 2.5, 3.9, 4.2, 5.7])

a = np.array([1.8, 2.5, 3.9, 4.2, 5.7])
new_a = a.astype(int)
print(a)
print(new_a)
print(new_a.dtype)

#2. 배열 만들기
#2.1 0이상 1 미만 실수 난수 : 2행 3열
#2.2 1이상 10 이하 정수 난수 : 3행 4열
#2.3 표준 정규분포 난수 : 2행 2열
from numpy.random import rand, randint, randn

b1 = rand(2, 3)
print(b1)

b2 = randint(1,11, size=(3,4))
print(b2)

b3 = randn(2,2)
print(b3)

#3. 배열 a = [10,20,30,40], b=[2,4,5,8]을 만들고 두 배열의 덧셈 뺼셈 곱셈 나눗셈을 각각 출력
a = np.arange(10,50,10)
b = np.array([2,4,5,8])

print(f"합 : {a+b}")
print(f"차 : {a-b}")
print(f"곱 : {a*b}")
print(f"나누기 : {a/b}")

#4 배열 [12,15,18, 20,25,30]의 합계, 평균, 최댓값, 최솟값, 중앙값, 표준편차를 각각 구하기
a = np.array([12,15,18,20,25,30])
print(f"합계 : {np.sum(a)}")
print(f"평균 : {np.mean(a)}")
print(f"최댓값 : {np.max(a)}")
print(f"최솟값 : {np.min(a)}")
print(f"중앙값 : {np.median(a)}")
print(f"표준편차 : {np.std(a)}")

#5 다음 2차원 배열의 전체 평균, 행별 평균, 열별 평균, 전체 합계, 행별 합계, 열별 합계를 구하기
a = np.array([[10,20,30],[40,50,60],[70,80,90]])

print(f"전체 평균 : {np.mean(a)}")
print(f"행별 평균 : {np.mean(a, axis=1)}")
print(f"열별 평균 : {np.mean(a, axis=0)}")
print(f"전체 합계 : {np.sum(a)}")
print(f"행별 합계 : {np.sum(a, axis=1)}")
print(f"열별 합계 : {np.sum(a, axis=0)}")

#6 다음 배열의 전체 최솟값, 행별 최솟값, 열별 최솟값, 전체 중앙값, 행별 중앙값, 열별 중앙값을 구하기
a = np.array([[8,3,5],[2,9,4],[7,1,6]])

print(f"전체 최솟값 : {np.min(a)}")
print(f"행별 최솟값 : {np.min(a, axis=1)}")
print(f"열별 최솟값 : {np.min(a, axis=0)}")
print(f"전체 중앙값 : {np.median(a)}")
print(f"행별 중앙값 : {np.median(a, axis=1)}")
print(f"열별 중앙값 : {np.median(a, axis=0)}")

#7 아래 배열에서 인덱싱가 슬라이싱으로 출력하기
a = np.arange(10,170,10).reshape(4,4)

#7.1 값 70
print(a[1,2])
#7.2 첫 번째 행 전체
print(a[0,:])
#7.3 세 번쨰 열 전체
print(a[:,2])
#7.4 오른쪽 아래 2행 2열
print(a[2:,2:])
#7.5 두번째~4번째 행, 두 번쨰 ~ 세번쨰 열
print(a[1:4, 1:3])

#8 행렬 A=[[1,2],[3,4]] B=[[5,6],[7,8]]에 대해 계산
A= np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
#8.1 A와 B의 행렬곱
print(A@B)

#8.2 A의 전치행렬
print(np.transpose(A))

#8.3 B의 전치행렬
print(np.transpose(B))

#8.4 A*B 와 A@B를 비교
print(f"A*B\n{A*B}")
print(f"A@B\n{A@B}")

#9 행렬 A[[4,7,],[2,6]]의 역행렬을 구하고, A와 그 역행렬을 곱해 결과 출력
A = np.array([[4,7],[2,6]])
B = np.linalg.inv(A)

print(np.round(A@B))

#10 아래 배열에서 각 행은 핵생, 각 열은 국어 영어 수학 성적
score = np.array([[80,90,70],[60,75,85],[95,80,90],[70,85,75]])

#10.1 전체 평균
print(np.mean(score))

#10.2 학생별 평균
print(np.mean(score, axis=1))

#10.3 과목별 평균
print(np.mean(score, axis=0))

#10.4 학생별 최솟값
print(np.min(score, axis=1))

#10.5 과목별 최댓값
print(np.max(score, axis=0))

#10.6 전체 중앙값
print(np.median(score))

#10.7 학생별 중앙값
print(np.median(score, axis=1))

#10.8 과목별 중앙값
print(np.median(score, axis=0))

#10.9 세 번쨰 학생의 수학 점수
print(score[2,2])

#10.10 첫 번째~ 두 번째 학생의 영어,수학 점수
print(score[0:2, 1:])