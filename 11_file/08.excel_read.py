"""
    pandas 라이브러리 : 데이터 분석 및 조작을 위한 라이브러리
        > CSV, Excel, json, SQL 등 다양한 형식의 데이터를 쉽게 읽어올 수 있음
        > 결측치(빈 데이터) 채우기/삭제, 중복 데이터 제거, 데이터 타입변환 등의 전처리 easy
        > 대용량 데이터도 빠르게 처리

    설치 필요: pip install pandas openpyxl
"""

import pandas as pd

# 엑셀 파일 읽어오기(첫 번째 시트를 기본으로 읽음)
df = pd.read_excel("11_file/data/students.xlsx")
#엑셀 파일에서 원하는 시트 불러오기
# pd.read_excel("11_file/data/students.xlsx", sheet_name="원하는 시트 이름(대소문자 확실히 구분해서 넣기)")

# print(df)
print(df.head()) #상위 5개 행만 불러옴

print("-"*30)

df = pd.read_json("11_file/data/data.json")
print(df)

print("-"*30)

df = pd.read_json("11_file/data/data_list.json")
print(df)

print("-"*30)

df = pd.read_json("11_file/data/data_list2.json")
print(df)

print("-"*30)

#일반 json 모듈로 파일을 읽어서 딕셔너리로 가져오기

import json

with open("11_file/data/data.json", "r", encoding="UTF-8")as f:
    data = json.load(f)

df = pd.DataFrame([data])
print(df)