from pathlib import Path

#읽어올 폴더 지정
data_dir = Path("11_file/output")

#폴더 안의 .txt 확장자를 모두 가져오기
txt_files = data_dir.glob('*.txt')

for file in txt_files:
    print("="*20+f'[파일 읽기: {file.name}]'+"="*20)
    with open(file, "r", encoding="UTF-8")as f:
        content = f.read()
        print(content)
    print("-"*50)