'''
# class(클래스)
  - 객체(사물)에 대한 속성과 기능을 코드로 구현한 것
  - class 클래스이름(첫글자 대문자):
        멤버 변수
        멤버 메서드(함수)

'''
# Student 클래스 정의
'''
class Student:
    name = "김하나"  #멤버 변수
    grade = 4

# 클래스 사용 
# 생성자 호출 - 인스턴스 생성
st1 = Student()
print(st1.name, st1.grade)
'''

# 생성자 사용 - __init__()
# self - 클래스안에서 멤버라는 의미의 키워드 필수.
# 함수의 매개변수로 반드시 필수적으로 기입함
'''
class Student:
    #기본 생성자
    def __init__(self):
        self.name = "콩쥐"
        self.grade = 1
        print("생성자 입니다.")

    def learn(self):
        print("수업을 들어요~")

# 생성자 호출 - 인스턴스 생성
s = Student() #s가 인스턴스
print(s) #객체의 메모리 주소 - <__main__.Student object at 0x000001F8F55C70E0>
print(type(s)) #<class '__main__.Student'>

print(f"{s.name} 학생은 {s.grade}학년입니다.")
s.learn()
'''

class Student:
    # 매개변수가 있는 생성자
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print(f"{self.name}가(이) 수업을 듣습니다.")

    # 객체의 정보를 출력하는 함수
    def __str__(self):
        return f"{self.name} 학생은 {self.grade}학년입니다."

'''   
# 매개변수 생성자 호출
st1 = Student("콩쥐", 2)
print(st1) #인스턴스(객체)의 정보 출력
st1.learn()

st2 = Student("팥쥐", 1)
print(st2)
st2.learn()
'''
# 학생 리스트 만들기
students = []  #빈 리스트 생성

st1 = Student("김하나", 1)
students.append(st1)

st2 = Student("이돌", 2)
students.append(st2)

st3 = Student("박열", 4)
students.append(st3)

# 첫번째 인덱스의 인스턴스 검색
print(students[0])
students[0].learn()

print("========== 학생 명단 ==========")
'''
n = len(students)
print(n) #3
for i in range(n):
    print(students[i])
    students[i].learn()
'''
for student in students:
    print(student)



