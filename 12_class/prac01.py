class Area:
    def calc_area(self, width, height):
        return width*height/2

class Score:
    def put_info(self):
        self.name = input("이름 입력: ")
        self.python = int(input("파이썬 점수 입력: "))
        self.ai = int(input("AI 점수 입력: "))

    def out_info(self):
        total = self.python + self.ai
        avg = total / 2
        print(f"이름 : {self.name}")
        print(f"파이썬 : {self.python}")
        print(f"AI : {self.ai}")
        print(f"합계 : {total}")
        print(f"평균 : {avg:.1f}")