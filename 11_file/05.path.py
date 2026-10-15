from pathlib import Path

target_file = Path("./output/result_data.txt")

target_file.parent.mkdir(parents=True, exist_ok=True)#폴더가 없으면 생성

with open(target_file, "w", encoding="UTF-8") as f:
    f.write("성공적으로 저장")