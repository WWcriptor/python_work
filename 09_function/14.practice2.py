price = [10000, 20000,30000,40000]
#20% 할인된 가격을 리스트에 넣기
new_price = [int((lambda x : x*0.8)(i)) for i in price]
print(new_price)