"""
    1. Phone 클래스
        생성자 __init__(self, phone_number): 전화번호를 받아 저장
        call(self, target_num) 메서드: "target_num 번호로 전화를 겁니다"를 출력

    2. Camera 클래스
        생성자 __init__(self, megapixels): 카메라 화소수(메가픽셀)를 받아 저장
        take_photo(self) 메서드: "megapixels만 화소로 사진을 촬영합니다"를 출력

    3. SmartPhone 클래스 (다중 상속)
        Phone과 Camera를 동시에 상속받음
        생성자 __init__(self, phone_number, megapixels, model_name): 두 부모의 초기화 메소드를 모두 호출하고
        스마트폰의 모델명(model_name)도 함께 저장
        show_info(self) 메서드 : 모델명, 전화번호, 카메라 화소수를 종합해서 출력
"""

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def call(self, target_number):
        print(f"{target_number} 번호로 전화를 겁니다.")

class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels

    def take_photo(self):
        print(f"{self.megapixels}만 화소로 사진을 촬영합니다.")

class SmartPhone(Phone, Camera):
    def __init__(self, phone_number, megapixels, model_name):
        Phone.__init__(self, phone_number)
        Camera.__init__(self, megapixels)
        self.model_name = model_name

    def show_info(self):
        print(f"모델명 : {self.model_name}, 전화번호 : {self.phone_number}, 카메라 성능 : {self.megapixels}만 화소")

if __name__ == "__main__":
    phone = SmartPhone("010-2299-4820", 2000, "갤럭시S26")
    phone.show_info()
    phone.call("010-4923-5284")
    phone.take_photo()