# 학생 6명의 영어 점수 관리
score = [70, 80, 50, 60, 90, 40]

n = len(score)
print(n) #6

# 요소에 접근(검색)
print(score[2]) #50
print(score[-1]) #40
print(score) #[70, 80, 50, 60, 90, 40]

# 요소 수정 - 80점을 90점으로 변경
score[1] = 90

# for i in range(시작값, 종료값, 증감값)
for i in range(0, n):
    print(score[i], end=" ")
print("\n========================")
# for item in 리스트이름
for item in score:
    print(item, end=" ") #70 90 50 60 90 40

# 성적의 평균 계산 = 합계 / 개수
total = 0
n = len(score)

# total = score[0] + score[1] + score[2] + score[3] + score[4] + score[5]
for i in range(0, n):  #(0, 6)
    total += score[i] #total = total + score[i]
print("\n총점:", total) #400
# 평균
average = total / n
print("평균:", average) #66.66666666666667
# round(숫자, 자리수) - 반올림
print("평균:", round(average, 1)) #66.7
# 서식 문자 - f(소수) - .1은 소수첫째 자리
print(f"평균: {average:.1f}") #66.7
'''
  i=0, 0 + 70,  total=70
  i=1. 70 + 90,  total=160
  i=2, 160 + 50, total=210
  i=3,
  i=4,
  i=5,
  i=6 반복 종료
 
'''
