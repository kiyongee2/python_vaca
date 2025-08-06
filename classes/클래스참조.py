# 참조 관계
'''
  학생 클래스가 과목 클래스를 참조하는 관계
'''

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
