#파일 열기

#전체 내용 읽어오기
# with open("test.txt", "r", encoding="UTF-8")as f:
#     text= f.read()
#     print(text)
#     t1 = text.split("\n")
#     print(t1)


#한 행만 읽어오기
# with open("test.txt", "r", encoding="UTF-8")as f:
#     text = f.readline()
#     print(text)


with open("test.txt", "r", encoding="UTF-8")as f:
    # text_line = f.readlines() #전체 내용을 한 행씩 읽어와서 리스트로 저장
    text_line = f.read().splitlines() # 1행씩 잘라주는 함수
    print(text_line)