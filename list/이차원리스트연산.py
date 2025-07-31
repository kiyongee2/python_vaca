# 2차원 리스트의 연산
"""
d2 = [
    [10, 20],
    [30, 40],
    [50, 60, 70]
]
total = 0  #합계
count = 0  #개수

# 계산 1
'''
for i in range(len(d2)): #range(0, 3)
    for j in range(len(d2[i])): #range(0, 2) or(0, 3)
        count += 1   #개수
        total += d2[i][j] #합계

  # 디버깅
  i=0, j=0, count=1, total=10
       j=1, count=2, total=10+20=30
  i=1, j=0, count=3, total=30+30=60
       j=2, count=4, total=60+40=100
  i=2, j=0, count=5, total=100+50=150
       j=1, count=6, total=150+60=210
       j=2, count=7, total=210+70=280
'''
# 계산2
for row in d2:
    for val in row:
        count += 1   #개수
        total += val #합계

print("개수:", count) #7
print("합계:", total) #280
print("평균:", total/count) #40.0
"""

# 학생 4명의 수학, 영어 성적 통계
score = [
    [80, 70],
    [80, 90],
    [50, 60],
    [70, 70]
]

# 개인별 총점과 평균
total = 0  #총점
n = len(score) #개수
print(n) #4

# 행(row)-변수, 열(상수)
print("*** 개인별 성적 통계 ***")
print("수학 영어 총점 평균")
for row in range(0, n):
    total = score[row][0] + score[row][1]
    print(f" {score[row][0]}  {score[row][1]}   {total}  {total/2}")

# 과목별 총점과 평균
sum_subject = [0, 0]     #수학, 영어 총점
avg_subject = [0.0, 0.0] #수학, 영어 평균

for row in range(0, n):
    sum_subject[0] += score[row][0] #수학 총점
    sum_subject[1] += score[row][1] #영어 총점

# 평균 점수 계산
avg_subject[0] = sum_subject[0] / n
avg_subject[1] = sum_subject[1] / n

print("*** 과목별 총점과 평균 ***")
print(f"수학 총점: {sum_subject[0]}점")
print(f"영어 총점: {sum_subject[1]}점")
print(f"수학 평균: {avg_subject[0]}점")
print(f"영어 평균: {avg_subject[1]}점")

