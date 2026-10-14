num = [i for i in range(5)]
print(num)

def inputNum(n):
    for i in n:
        n[i] = int(input(f"{i+1}번쨰 정수 입력"))

inputNum(num)
# print(num)

def outputNum(n):
    print("-"*10+"출력"+"-"*10)
    for i, v in enumerate(n):
        print(n[i], end=" ")
        # print(v, end=" ")

outputNum(num)