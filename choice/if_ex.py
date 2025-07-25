# 조건문 - if문
# 콜론(:) - 코드 블럭을 의미함
# 콜론 다음 줄은 4칸 들여쓰기(indent)라고 함
# 조건 - 나이가 15세 이상이면 "관람가", 아니면 "관람 불가"
'''
age = 17

if age >= 15:
    print("관람가")
else:
    print("관람불가")

print("나이는 " + str(age) + "세 입니다.")
'''

# 2의 배수 - 2로 나눈 나머지가 0이다.(나누어 떨어진다)
# 6 % 2 == 0, 7 % 2 == 1
# 짝수/홀수를 판별하는 프로그램
'''
x = int(input("정수 입력: "))
#x = int(x)

if x % 2 == 0:
    print("짝수")
else:
    print("홀수")
'''

# 좌석의 줄수를 계산하는 프로그램
"""
# 나누어 떨어진다.
# row = customer // column #20 // 5 = 4
# 나누어 떨어지지 않은 경우
# row2 = customer /column + 1  #20 / 5 + 1
"""
'''
customer = int(input("입장객 수: ")) #입장객 수
column = int(input("좌석 열 수: "))  #좌석 수

if customer % column == 0:
    #row = customer // column
    row = int(customer / column)
else: #나누기는 실수형이므로 정수형으로 변환
    row = int(customer / column) + 1  

print(str(row) + "개의 줄이 필요합니다.") 
'''

# 조건 - 자격증을 획득하는 프로그램
# 필기는 60점 이상이고, 실기는 70점 이상이면 "자격증 취득", 아니면 "미취득"
# 중첩 if문
필기 = 65
실기 = 80

'''
if 필기 >= 60 and 실기 >= 70:
    print("자격증 취득")
else:
    print("자격증 미취득")

'''

if 필기 >= 60:
    print("필기 시험 합격")
    if 실기 >= 70:
        print("실기시험 합격 및 자격증 취득")
    else:
        print("실기시험 불합격 및 자격증 미취득")
else:
    print("필기 시험 불합격")
























