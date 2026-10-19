"""
    은행: 개설할 때 계좌주 이름과 초기 예금액을 입력받아 넣는다.
          입금하면 잔고 변경
          출금 잔고 변경(잔액보다 많이 출금할 수 없음)        
"""

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("잔액이 부족합니다")

    def getBalance(self):
        return self.__balance

book = Bank("박휘숙", 1000000)
book.deposit(300000)
book.withdraw(2000000)
book.withdraw(50000)
print(book.getBalance())