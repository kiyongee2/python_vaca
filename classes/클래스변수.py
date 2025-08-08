'''
  - 클래스 변수의 위치는 __init__() 위에 위치
  - 클래스 변수는 클래스 이름으로 직접 접근함
'''
class Dog:
    kind = "진돗개"  #클래스 변수

    def __init__(self, name):
        self.name = name #인스턴스(멤버) 변수

    def __str__(self):
        return f"강아지 이름: {self.name}"

'''   
# Dog 인스턴스 생성
dog1 = Dog("백구")
dog2 = Dog("콜라")

print(dog1)
print(dog2)

# print(dog1.kind)
# Dog(클래스) 이름으로 직접 접근
print(Dog.kind) #모든 dog이 공유
'''

# 카운터(Counter) 만들기
'''
   카운터는 숫자가 1, 2, 3..증가함
'''

# 인스턴스형 카운터
'''
class Counter:
    def __init__(self):
        self.x = 0 
        self.x += 1 #x에 1을 더함

    def get_count(self):
        return self.x
    
# Counter 생성자 호출
c1 = Counter()
print(c1.get_count()) #1

c2 = Counter()
print(c2.get_count()) #1

c3 = Counter()
print(c3.get_count()) #1
'''

# 클래스형 카운터
class Counter:
    x = 0  #클래스 변수(전역 변수), global 변수

    def __init__(self):
        Counter.x += 1  #클래스이름으로 접근
        # self.x += 1 #값이 공유되지 않음

    def get_count(self):
        return self.x

''' 
# Couter의 생성자 호출
c1 = Counter()
print(c1.get_count()) #1

c2 = Counter()
print(c2.get_count()) #2

c3 = Counter()
print(c3.get_count()) #3
'''

# 변수값 교환하기
'''
x = 1
y = 2

print("x =", x, ", y =", y)

# 교환
#방법1
# x, y = y, x 

# 방법2
temp = x
x = y
y = temp

print("x =", x, ", y =", y)
'''

class Cls:
    # x = 1
    # y = 2
    x, y = 1, 2 #전역(클래스) 변수, 구조 분할

    #기본 생성자 생략
    def change(self): #교환 방법1
        self.x, self.y = self.y, self.x

    def change2(self): #교환 방법2
        temp = self.x 
        self.x = self.y 
        self.y = temp

'''
# Cls의 생성자 호출
c1 = Cls()
print(f"x = {c1.x}, y = {c1.y}") #x=1, y=2

c1.change() #교환 함수 호출
print(f"x = {c1.x}, y = {c1.y}") #x=2, y=1

c2 = Cls()
c2.change2()
print(f"x = {c2.x}, y = {c2.y}") #x=2, y=1
'''

# 연습 문제
class City:
    a = ['Seoul', 'Inchon', 'Daejon', 'Jeju']

# 클래스 리스트(a)는 클래스 이름으로 접근 
# print(City.a) #['Seoul', 'Inchon', 'Daejon', 'Jeju']

str = '' #문자를 저장할 변수 초기화
for i in City.a:
    # print(i)
    str += i[0]

print(str) #SIDJ