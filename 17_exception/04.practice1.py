"""
    custom except
    1. 이미 예약된 좌석을 선택했을 때
    2. 없는 좌석 번호로 예약할 떄

    class
    1. 초기화 영화제목, 총 좌석
    2. 좌석이 유효한 좌석인지
        좌석이 있으면 예약이 됨 / 없는 좌석일 경우 예외 발생
    3. 예약
        예약하기. 이미 예약된 상태일 경우 예외 발생
    4. 예약 취소
    5. 출력(영화 : ??? / 예약된 좌석: ???)
"""

class ReservationError(Exception):
    def __init__(self,seet):
        super().__init__(f"{seet}좌석은 이미 예약된 좌석입니다.")

class NoneSeatError(Exception):
    def __init__(self):
        super().__init__("존재하지 않는 좌석입니다.")

class NotReserveError(Exception):
    def __init__(self):
        super().__init__("예약이 확인되지 않습니다.")

class Movie:
    def __init__(self, title, seets):
        self.title = title
        self.seets = seets
        self.reserve=[]

    def reservation(self, num):
        if num > self.seets or num <= 0:
            raise NoneSeatError()
        if num in self.reserve:
            raise ReservationError(num)
        self.reserve.append(num)
        print(f"{num}번 좌석이 성공적으로 예매되었습니다.")
    
    def cancel(self, num):
        if num not in self.reserve:
            raise NotReserveError()
        self.reserve.remove(num)
        print(f"{num}번 좌석의 예약 취소가 성공적으로 이루어졌습니다.")

    def show_reservation(self):
        print(f"영화 : {self.title}")
        print(f"예약된 좌석 : {self.reserve}")
        

try:
    parasite = Movie("기생수", 50)
    parasite.reservation(3)
    # parasite.cancel(3)
    # parasite.cancel(3)
    parasite.reservation(60)
except (NoneSeatError, ReservationError,NotReserveError) as e:
    print(e)

parasite.show_reservation()

