"""
    은행: 개설할 때 계좌주 이름과 초기 예금액을 입력받아 넣는다.
          입금하면 잔고 변경
          출금 잔고 변경(잔액보다 많이 출금할 수 없음)    

          [???님의 계좌 정보] 현재 잔액 : ???원    
"""

class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance
        print(f"{self.name}님의 계좌가 개설되었습니다. 현재 잔액: {self.__balance}원")

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount}원이 입금되었습니다.")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"{amount}원이 출금되었습니다.")
        else:
            print(f"인출하시려는 금액: {amount}원")
            print(f"현재 잔액: {self.__balance}원")
            print("잔액이 부족합니다")

    def getBalance(self):
        return self.__balance

    def __str__(self):
        return f"[{self.name}님의 계좌 정보] 잔액: {str(self.__balance)}원"

book1 = Bank("박휘숙", 1000000)
book2 = Bank("김철수")
book1.deposit(300000)
book2.deposit(20000)
book1.withdraw(2000000)
book1.withdraw(50000)
book2.withdraw(10000)
print(book1)
print(book2)