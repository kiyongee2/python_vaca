# 상속(inheritance)
'''
  이미 정의된 클래스를 상속 받아서
  속성이나 기능이 확장되는 클래스를 구현하는 것
  - class 클래스 이름(상속할 클래스이름)
'''
class Person:
    def __init__(self, name): #생성자
        self.name = name

    def greet(self):
        print(f"안녕하세요. 성명: {self.name}", end='')

    def __str__(self): #인스턴스의 문자열 정보
        return f"<Person name: {self.name}>"

# Person을 상속받은 Employee
class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)  #부모 클래스의 생성자 호출
        self.id = id

    def greet(self):
        super().greet()  #부모 클래스의 greet() 호출
        print(f", 사번은 {self.id}입니다.")

    def __str__(self):
        return f"<Employee name: {self.name}, id: {self.id}>"
    
# Person의 인스턴스 생성
p1 = Person("이종범")
# print(p1)
p1.greet()
print()

e1 = Employee("이정후", 51)
# print(e1)
e1.greet()