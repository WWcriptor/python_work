py = 3
d = 2
ai = 3

py_grade = 4.5
d_grade = 3.0
ai_grade = 4.0

total = (py*py_grade + d*d_grade + ai*ai_grade)/(py+d+ai)

print(f"이수학점은 {py+d+ai}점 이고, 학점 평균은 {total:.2f}점 입니다")