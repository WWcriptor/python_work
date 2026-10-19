class Calculator:
    def plus(self, x, y):
        return x+y

    def minus(self, x, y):
        return x-y

    def mul(self, x, y):
        return x*y

    def divide(self, x, y):
        return x/y

if __name__ == "__main__": #현재 파일이 메인 스레드일 때만 실행
    cal = Calculator()
    print(cal.plus(3,5))