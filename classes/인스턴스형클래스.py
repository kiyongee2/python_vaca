# 자동차 클래스 정의와 사용
"""
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
    
# 인스턴스 생성을 위한 호출
car1 = Car("스포티지", 2020)
car1.drive()
print(car1)

car2 = Car("EV6", 2023)
car2.drive()
print(car2)
"""

# 계산기 클래스 정의와 사용
class Calculator:
    def __init__(self):
        self.x = 0  #멤버변수 x를 초기화

    def add(self, y):
        self.x += y #self.x = self.x + y
        return self.x
    
    def sub(self, y):
        self.x -= y
        return self.x
    
    def mul(self, y):
        self.x *= y
        return self.x
    
    def div(self, y):
        if y != 0:
            self.x /= y
        else:
            print("Error: 0으로 나눌 수 없습니다.")
        return self.x

# 기본 생성자 호출   
cal = Calculator()
print(cal.add(10))  #10
print(cal.sub(4))   #6
print(cal.mul(2))   #12
# print(cal.div(10))  #1.2
print(cal.div(0))   #12
