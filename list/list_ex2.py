# 정수형 리스트 생성 - 성적 관리
score = [70, 80, 60, 90]
total = 0  # 총점
count = 0  # 개수

# 리스트의 개수 - len()
count = len(score)
print("리스트의 개수:", count) # 4

# 1번 위치 검색
print(score[1])

# 점수 더하기
print(score[0] + score[1]) #150

# 총점 계산하기
for i in score:
    total += i #total = total + i
print("총점:", total) #300

# 평균 계산하기
average = total / count
print("평균:", average) # 75.0

# 전체 출력
for i in score:
    print(i)

