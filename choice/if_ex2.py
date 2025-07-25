"""
# 다중 조건문
# if ~ elif ~ else
# 놀이 공원 입장료 계산
  - 취학전 아동(1 ~ 7) - 1000
  - 초등학생(8 ~ 13) - 2000
  - 중,고등학생(14 ~ 19) - 2500
  - 일반인(20 ~) - 3000
# 오류 - "범위를 초과했어요. 다시 입력하세요"

age = int(input("나이 입력(1 ~ 100 입력): "))
admisson_fee = 0 #입장료

if age <= 0 or age > 100:
    print("범위를 초과했어요. 다시 입력하세요")
else:
    # 정상 영역
    if age >= 1 and age < 8:
        print("미취학 아동입니다.")
        admission_fee = 1000
    elif age >= 8 and age < 14:
        print("초등 학생입니다.")
        admission_fee = 2000
    elif age >= 14 and age < 20:
        print("중,고등 학생입니다.")
        admission_fee = 2500
    else:
        print("일반인 입니다.")
        admission_fee = 3000

    print("입장료는 " + str(admission_fee) + "원 입니다.")

"""

# 학점 계산 프로그램
score = int(input("점수를 입력하세요(0 ~ 100): "))

if score < 0 or score > 100:
    print("유효한 점수를 입력하세요")
else:
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = 'B'
    elif score >= 70 and score < 80:
        grade = 'C'
    elif score >= 60 and score < 70:
        grade = 'D'
    else:
        grade = 'F'

    print("학점은 " + grade + "입니다")























