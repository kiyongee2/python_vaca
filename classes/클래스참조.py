# 참조 관계
'''
  학생 클래스가 과목 클래스를 참조하는 관계
'''
# Subject 클래스 정의
class Subject:
    def __init__(self):
        self.subject_name = ""  #과목명
        self.subject_score = 0  #점수

    # 과목명 입력 메서드
    def set_subject_name(self, subject_name):
        self.subject_name = subject_name

    # 과목명 반환 메서드
    def get_subject_name(self):
        return self.subject_name
    
    # 점수 입력 메서드
    def set_subject_score(self, subject_score):
        self.subject_score = subject_score

    # 점수 반환 메서드
    def get_subject_score(self):
        return self.subject_score
    
# Student 클래스 정의
class Student:
    #생성자
    def __init__(self, student_id, student_name):
        self.student_id = student_id      #학번
        self.student_name = student_name  #이름
        # Subject 생성자 호출
        self.korean = Subject()   #국어 과목
        self.math = Subject()     #수학 과목

    # 국어 과목 설정
    def set_korean_subject(self, name, score):
        self.korean.set_subject_name(name) #과목명 입력함수 호출
        self.korean.set_subject_score(score) #과목점수 입력함수

    # 수학 과목 설정
    def set_math_subject(self, name, score):
        self.math.set_subject_name(name)
        self.math.set_subject_score(score)

    # 평균 점수 계산
    def calc_average(self):
        return (self.korean.get_subject_score() + 
                self.math.get_subject_score()) / 2

    # 학생의 정보 출력
    def print_info(self):
        print(f"학번: {self.student_id}")
        print(f"이름: {self.student_name}")
        print(f"{self.korean.get_subject_name()} \
점수: {self.korean.get_subject_score()}")
        print(f"{self.math.get_subject_name()} \
점수: {self.math.get_subject_score()}")
        print(f"평균 점수: {self.calc_average()}")
        print("-------------------------")

# Student 인스턴스 생성 
'''
lee = Student(101, "이정후")
lee.set_korean_subject("국어", 85)
lee.set_math_subject("수학", 88)
lee.print_info()
'''

# 리스트로 관리
students = []

# 1명 생성
lee = Student(101, "이정후")
lee.set_korean_subject("국어", 85)
lee.set_math_subject("수학", 88)
students.append(lee)

# 2명 생성
shin = Student(102, "신유빈")
shin.set_korean_subject("국어", 90)
shin.set_math_subject("수학", 93)
students.append(shin)

print("===== 성  적  표 =====")
for student in students:
    student.print_info()


