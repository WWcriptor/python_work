import random

# f = random.random()
# x = random.randint(1,6) #end 포함
# print(f)
# print(x)

"""
    주사위 3개를 동시에 던져서 3개가 다 동일한 숫자가 나오면 탈출
    주사위에 나온 숫자와 횟수 출력
"""
# turn = 0

# while True:
#     turn +=1
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     dice3 = random.randint(1,6)

#     print(f"{turn:3d}회 : {dice1, dice2, dice3}")

#     if dice1 == dice2 and dice2 == dice3:
#         break

"""
    주사위 숫자 맞추기
"""

turn = 0

while True:
    turn+=1
    num = int(input("주사위 숫자를 입력하세요(끝내려면 0) : "))
    if num == 0:
        break

    if num < 1 or num > 6:
        print("주사위 숫자는 1부터 6까지 입니다.")
        turn -= 1
        continue

    dice = random.randint(1,6)
    print(f"{turn}회 진행 결과")
    print(f"고른 숫자 : {num}, 나온 숫자 : {dice}\n")

    if num == dice:
        print(f"{turn}회 째에 성공하셨습니다")
        break