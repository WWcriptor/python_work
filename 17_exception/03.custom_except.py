#나만의 커스텀 에러를 만들어 사용

#방법 1 : 에러 메시지를 던잴 때 직접 입력받도록 하기

#커스텀 에러 클래스
# class BalanceError(Exception):
#     def __init__(self, message = "계좌의 잔액이 부족하여 출금할 수 없습니다."):
#         super().__init__(message)


# # 입금 함수
# def diposit(balance, amount):
#     if amount <= 0:
#         raise BalanceError(f"{amount}원 입금 불가")
#     balance += amount
#     print(f"{amount}원 입금 완료. 현재 잔액 : {balance}원")
#     return balance

# #출금 함수
# def withdraw(balance, amount):
#     if balance <amount:
#         raise BalanceError()

#     balance -= amount
#     return balance

# try:
#     current_balance = 5000
#     current_balance = diposit(current_balance, 3000)
#     current_balance = withdraw(current_balance, 10000)

# except BalanceError as e:
#     print(f"[뱅킹 오류] {e}")

#방법 2
#출금용가 입금용 커스텀 에러 클래스를 따로 정의

class BalanceOutputError(Exception):
    def __init__(self):
        super().__init__("계좌의 잔액이 부족하여 출금할 수 없습니다.")

class BalanceInputError(Exception):
    def __init__(self):
        super().__init__("0원 이하는 입금할 수 없습니다.")

# 입금 함수
def diposit(balance, amount):
    if amount <= 0:
        raise BalanceInputError
    balance += amount
    print(f"{amount}원 입금 완료. 현재 잔액 : {balance}원")
    return balance

#출금 함수
def withdraw(balance, amount):
    if balance <amount:
        raise BalanceOutputError()

    balance -= amount
    return balance

try:
    current_balance = 5000
    current_balance = diposit(current_balance, 3000)
    current_balance = withdraw(current_balance, 10000)

except (BalanceInputError, BalanceOutputError) as e:
    print(f"[뱅킹 오류] {e}")