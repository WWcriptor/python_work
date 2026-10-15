#키워드 인자

def display_info(academy, name, classroom):
    print(f"Academy :{academy}, Name : {name}, classroom : {classroom}")

display_info("더조은","나","704")

def display_info2(name, classroom, academy="더좋은"): #디폴트 값이 있는 건 무조건 뒤에
    print(f"Name : {name}, classroom : {classroom}, Academy :{academy}")

display_info2("나나난", "704호")

#순서와 무관하게 나오게 하려면
display_info2(name="이츠미", classroom="703호", academy="아카데미")