import json

#인코더 자동 선택 함수
def enco(file_path):
    encodings = ['UTF-8', 'EUC-KR', 'CP949']

    for enc in encodings:
        try:
            with open(file_path, "r", encoding=enc)as f:
                return enc
        except UnicodeDecodeError:
            continue

#data.json : 한 개의 {}만 있을 때 파일 가져오기
files = "11_file/data/data.json"
with open(files, "r", encoding=enco(files))as f:
    data = json.load(f)

print(data)
print(type(data))
print(data.keys())
print(f"이름 : {data["name"]}")
print(f"보유기술 : {data["skills"]}")

print("-"*90)
#data2.json : 여러개의 {}가 있을 때 파일 가져오기
students =[]
add_string = ""
files = "11_file/data/data2.json"
with open(files, "r", encoding=enco(files))as f:
    for line in f:
        line = line.strip()
        add_string += line

        if line == "}":
            student_dic = json.loads(add_string)
            students.append(student_dic)
            add_string = ""

print("====== [변환된 students 리스트] ======")
print(students)
print("====== [한 명씩 출력] ======")
for std in students:
    # print(f"이름 : {std["name"]} | 나이 : {std["age"]}세 | 보유기술 : {std["skills"]}")
    print(f"이름 : {std["name"]} | 나이 : {std["age"]}세 | 보유기술 : {",".join(std["skills"])}")

print("-"*90)
#data3.json : 여러개의 {}가 줄바꿈이 있을 때
add_string = ""
students =[]

files = "11_file/data/data3.json"
with open(files, "r", encoding=enco(files))as f:
    for line in f:
        if not line:  #바닥(빈 행)인가?
            continue

        line = line.strip()
        add_string += line

        if line == "}":
            student_dic = json.loads(add_string)
            students.append(student_dic)
            add_string = ""

print("====== [변환된 students 리스트] ======")
print(students)
print("====== [한 명씩 출력] ======")
for std in students:
    # print(f"이름 : {std["name"]} | 나이 : {std["age"]}세 | 보유기술 : {std["skills"]}")
    print(f"이름 : {std["name"]} | 나이 : {std["age"]}세 | 보유기술 : {",".join(std["skills"])}")

            
