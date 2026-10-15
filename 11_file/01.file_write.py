"""
    파일 다루기
        파일 열기 -> 파일을 읽거나 쓰기 -> 파일 닫기
        open("파일명", "모드") -> write("문자열") -> close() or with
"""

#파일 열기
f = open("test.txt", "w", encoding="UTF-8")
#파일에 데이터 쓰기
# f.write("데이터 출력\n")
# f.write("5") #무조건 문자열로만 넣어야 함
# f.write("True")

for i in range(1,11):
    f.write(f"{i}번째 줄 입니다.\n")

f.close()
print("쓰기 완료")

with open("with_test.txt","w", encoding="UTF-8") as g:
    for i in range(1,11):
        g.write(f"{i}번째 줄 입니다.\n")