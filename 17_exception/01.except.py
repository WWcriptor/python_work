"""
    예외처리 : try - except - finally
"""

try:
    #예외가 발생할 가능성이 있는 코드
    result = 10/0
    print(result)
    print("try에서 실행됨")
except:
    #예외가 발생했을 때 실행할 코드
    print("오류 발생")

print("프로그램 끝")


# try:
#     num = int(input("숫자 입력: "))
#     result = 10/ num
# except ValueError:
#     print("숫자만 입력해야 합니다.")
# except ZeroDivisionError as z:
#     print(f"0으로 나눌 수 없습니다.(에러 메시지 : {z})")

try:
    f = open("17_exception/data.txt", "r")
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
else:
    print("파일을 성공적으로 읽었습니다.")
finally: #오류가 발생해도 실행됨
    print("작업을 끝냅니다.")