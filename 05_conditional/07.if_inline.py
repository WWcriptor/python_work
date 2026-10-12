#삼항 연산식(참이면 앞에 거, 거짓이면 뒤에 것)

num = 2

print("2입니다") if num == 2 else print("2가 아닙니다")
print("2입니다" if num == 2 else "2가 아닙니다")


#합격 불합격
#일반 조건문

score = 75

if score >60:
    result = "합격"
else:
    result = "불합격"

print("합격" if score > 60 else "불합격")
result = "합격" if score > 60 else "불합격"
print(result)


# 두 수 중 큰 숫자 찾기

num1 = 42
num2 = 39

max_num = num1 if num1 > num2 else num2
print(f"{num1}과 {num2} 중 큰 숫자는 {max_num}입니다")

#회문 : 어느 방향에서 읽어도 같은 문자열

str = "aibohphobiadklag"
if str == str[::-1]:
    print(f"{str} : 회문입니다")
else:
    print(f"{str} : 회문이 아닙니다")
print(str, ": 회문" if str == str[::-1] else ": 회문아님")
print(f"{str} : 회문" if str == str[::-1] else f"{str} : 회문아님")
print(f"{str} : {'회문' if str == str[::-1] else '회문아님'}")