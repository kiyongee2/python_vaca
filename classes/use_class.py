# myclass 모듈 사용하기
from my_lib.myclass import Car, Cart

# Car 생성자 호출
car1 = Car("EV6", 2023)
print(car1)
car1.drive()

# Cart 생성자 호출
cart1 = Cart("한강")
cart1.add("식빵", "딸기쨈", "커피", "바나나")
print(cart1)

cart1.remove("바나나")
print(cart1) #한강의 장바구니: ['식빵', '딸기쨈', '커피']

print("장바구니 품목의 개수:", len(cart1.items))