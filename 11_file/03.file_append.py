#추가모드로 열기
# with open("test.txt", "a", encoding="UTF-8")as f:
#     f.write("이어쓰기\n")

#     for i in range(11,21):
#         f.write(f"{i}번째 이어쓰기 \n")

# print("쓰기 완료")

with open("text.txt", "x", encoding="UTF-8")as f: #배타적 어쩌구 모드. 파일이 있으면 오류남
    f.write("집에 언제 가")

print("쓰기 완료")