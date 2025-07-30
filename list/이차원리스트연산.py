# 2차원 리스트의 연산
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
        count += 1
        total += val

print("개수:", count) #7
print("합계:", total) #280
print("평균:", total/count) #40.0

