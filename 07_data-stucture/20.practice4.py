"""
    로또 프로그램 만들기
    사용자로부터 몇 회 분 살 건지 물어보고
    그 횟수만큼 번호를 랜덤으로 추출하여 출력하기
"""
import random

turn = int(input("몇 번 구매하나요? : "))


for i in range(turn):
    lotto = set()
    while len(lotto) != 6:
        lotto.add(random.randint(1,45))

    lotto_list = sorted(lotto)
    print(lotto_list)   

