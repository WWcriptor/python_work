"""
    한 과일 가게의 현재 과일 재고 수량이 다음과 같이 딕셔너리에 저장되어 있다.
    inventory = {
        'apple' : 15,
        'banana' : 8,
        'orange' : 20,
        'melon' :3
    }
    Q1. 가게에 포도('grape')가 12개 새로 들어왔다. 추가하기
    Q2. 손님이 망고('mango')가 있는지 물어보았다. 망고가 있으면 재고 출력, 
    없으면 '재고가 없습니다' 출력
    Q3. 오늘 마감 전, 현재 가게에 남아있는 모든 과일의 이름과 재고 수량을 
    아래의 보기와 같은 형식으로 한 줄씩 출력하는 코드를 작성
    (단, item() 메서드와 for문, f-string을 반드시 사용)
    [출력 보기]
    과일: apple | 재고: 15개
    과일: banana | 재고: 8개
    . . .
"""
inventory = {
    'apple' : 15,
    'banana' : 8,
    'orange' : 20,
    'melon' : 3
}

if 'grape' in inventory:
    inventory['grape'] += 12
else:
    inventory['grape'] = 12
print(inventory)

if 'mango' in inventory:
    print(f"망고 재고가 {inventory['mango']}개 있습니다")
else:
    print("재고가 없습니다.")

mango_count = inventory.get('mango', "재고가 없습니다.") #인벤토리에서 망고를 가져옴 없으면 작성한대로
print(mango_count)


for key, value in inventory.items():
    print(f"과일: {key} | 재고: {value}개")