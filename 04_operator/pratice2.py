"""
문제
제품 | 구매가 | 판매가
캔 커피 | 500 | 1800
삼각김밥 | 900 | 1400
바나나 우유 | 800 | 1800
도시락 | 3500 | 4000
콜라 | 700 | 1500
새우깡 | 1000 | 2000

삼각김밥 10개 구입
바나나 우유 2개 판매
도시락 5개 구입
도시락 4개 판매
콜라 1개 판매
새우깡 4개 판매
캔커피 5개 판매
"""

coffe_buy = 500
coffe_sell = 1800
kim_buy = 900
kim_sell = 1400
milk_buy = 800
milk_sell = 1800
bento_buy = 3500
bento_sell = 4000
coke_buy = 700
coke_sell = 1500
snak_buy = 1000
snak_sell = 2000

balance = 100000
sell = 0
buy = 0

coffe_buy_count = int(input("캔 커피 구매 개수 : "))
coffe_sell_count = int(input("캔 커피 판매 개수 : "))
kim_buy_count = int(input("삼각김밥 구매 개수 : "))
kim_sell_count = int(input("삼각김밥 판매 개수 : "))
milk_buy_count = int(input("바나나 우유 구매 개수 : "))
milk_sell_count = int(input("바나나 우유 판매 개수 : "))
bento_buy_count = int(input("도시락 구매 개수 : "))
bento_sell_count = int(input("도시락 판매 개수 : "))
coke_buy_count = int(input("콜라 구매 개수 : "))
coke_sell_count = int(input("콜라 판매 개수 : "))
snak_buy_count = int(input("새우깡 구매 개수 : "))
snak_sell_count = int(input("새우깡 판매 개수 : "))

buy += (coffe_buy_count*coffe_buy)+(kim_buy_count*kim_buy)+(milk_buy_count*milk_buy)+(bento_buy_count*bento_buy)+(coke_buy_count*coke_buy)+(snak_buy_count*snak_buy)
sell += (coffe_sell_count*coffe_sell)+(kim_sell_count*kim_sell)+(milk_sell_count*milk_sell)+(bento_sell_count*bento_sell)+(coke_sell_count*coke_sell)+(snak_sell_count*snak_sell)

balance += sell
balance -= buy

print(f"오늘 판매 총액은 {sell}원 이고, 구매 총액은 {buy}원 입니다. 남은 금액은 {balance} 순 수익은 {sell-buy}원 입니다.")