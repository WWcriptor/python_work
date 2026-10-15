"""
    기본환경 : 모든 개발환경에 공통적으로 설치됨
    가상환경 : 해당 프로젝트에서만 사용하는 패키지 설치

    가상환경 만들기
    터미널에서 python -m venv 가상환경이름

    가상환경 활성화
    cmd) 가상환경이름(역슬래시)Scripts(역슬래시)activate

    가상환경 종료
    cmd) deactivate

    > 외부 라이브러리 중 request
    requests는 외부 웹페이지에 접근하여 응답을 받아오는 http통신 라이브러리
"""
import requests

def get_ex():
    response = requests.get("https://google.com")
    print(f"Status Code : {response.status_code}")
    # print(response.text)

if __name__ == "__main__":
    get_ex()
