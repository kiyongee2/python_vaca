# 자동차 클래스
class Car:
    # 생성자
    def __init__(self, model, year):
        self.model = model   #모델명
        self.year = year     #연식

    def drive(self):
        print(f"{self.model}가 달립니다.")

    # 객체의 정보를 문자열로 반환
    def __str__(self):
        return f"모델명: {self.model}, 연식: {self.year}"

'''
if __name__ == "__main__":
    # car 인스턴스 생성
    car = Car("소나타", 2025)
    print(car)
    car.drive()
'''

# 쇼핑몰 장바구니 클래스
class Cart:
    #생성자
    def __init__(self, user):
        self.user = user
        self.items = []   #장바구니 리스트 생성

    # 품목 추가 기능
    def add(self, *goods): # 가변매개변수(변수앞에 *을 붙임)
        self.items.extend(goods) #extend([리스트 형태])

    # 품목 삭제 기능
    def remove(self, item):
        if item in self.items: #장바구니에 포함된 아이템
            self.items.remove(item) #삭제

    # 정보 출력
    def __str__(self):
        return f"{self.user}의 장바구니: {self.items}"

if __name__ == "__main__":
    # Cart 생성자 호출
    my_cart = Cart("우영우")

    # 장바구니에 품목 추가
    my_cart.add("계란", "라면", "콩나물")

    # 장바구니 정보 출력
    print(my_cart) #우영우의 장바구니: ['계란', '라면', '콩나물']

    # 장바구니 품목 삭제
    my_cart.remove("라면")

    print(my_cart) #우영우의 장바구니: ['계란', '콩나물']

    # 장바구니 품목의 개수 출력
    print("장바구니 품목의 개수:", len(my_cart.items))

