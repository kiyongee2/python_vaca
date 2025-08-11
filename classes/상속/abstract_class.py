# 추상 클래스
'''
  - 추상 메서드(함수)를 포함하고 있는 클래스
  - 추상메서드는 구현할 수 없고 선언만 할수 있는 메서드
'''

class Animal:
    # 생성자 생략 - 기본 생성자
    def breathe(self):
        print("동물이 숨을 쉽니다.")

    # 울음 소리는 구현할 수 없음
    # 상속받은 클래스 반드시 구현해야 함(필수)
    # 예외(오류)를 미뤄놓음(연기 시킴)
    def cry(self):
        raise NotImplementedError("반드시 구현해야 합니다.")

# Animal을 상속 받은 Dog 클래스
class Dog(Animal):
    def cry(self):
        print("왈~ 왈~")

class Cat(Animal):
    # def cry(self):
    #     print("야~ 옹!")
    pass

try:
    dog = Dog()
    dog.breathe()
    dog.cry()

    cat = Cat()
    cat.breathe()
    cat.cry()
except NotImplementedError as e:
    print(f"오류: {e}")