# 최대값 찾기
# 두 수중에서 큰 값 찾기
'''
x, y = 10, 20

# 더 큰값을 저장할 변수 - max_v
if x > y:
    max_v = x
else:
    max_v = y
print("더 큰값:", max_v)

# 파이썬 내장함수 - max(), min()
print("더 큰값:", max(x, y))
'''

# 세개의 숫자 중에서 최대값 구하기
'''
a, b, c = 1, 2, 3

# 첫번째 값을 최대값으로 설정함 
max_v = a
if b > max_v:
    max_v = b
if c > max_v:
    max_v = c

print("최대값:", max_v) #3
'''
# 최대값 계산 함수 정의
'''
def max3(a, b, c):
    max_v = a
    if b > max_v:
        max_v = b
    if c > max_v:
        max_v = c
    return max_v #최대값을 호출한 함수에 반환

print(f"max3(2, 1, 3) = {max3(2, 1, 3)}") #3
print(f"max3(2, 3, 1) = {max3(2, 3, 1)}") #3
'''
# 성적 리스트에서 최대값 찾기
'''
score = [80, 70, 50, 90, 70]

# 첫째 위치의 값을 최대값으로 정한다.
max_v = score[0]
n = len(score) #개수만큼 반복
for i in range(n):
    if score[i] > max_v:
        max_v = score[i]

print("최대값:", max_v)
'''
# 최대값 계산 함수
"""
def find_max(a):
    max_v = a[0] #최대값 지정
    n = len(a) #개수만큼 반복
    for i in range(n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

# 최대값의 위치 찾기
def find_max_idx(a):
    max_idx = 0  #최대값을 0번 위치로 정함
    n = len(a)
    for i in range(n): #0 ~ n
        if a[i] > a[max_idx]: 
            max_idx = i
    return max_idx

'''
   i=0, a[0]>a[0], 80>80, max_idx=0
   i=1, a[1]>a[0], 70>80, max_idx=0
   i=2, a[2]>a[0], 50>80, max_idx=0
   i=3, a[3]>a[0], 90>80, max_idx=3
'''
# 성적 리스트 생성
score = [80, 70, 50, 90, 70]

# 최대값 찾기 함수 호출
max_score = find_max(score)
print("최대값:", max_score) 

# 최대값 위치 찾기 함수 호출
max_score_idx = find_max_idx(score)
print("최대값의 위치:", max_score_idx)

# 파이썬에서 제공하는 max(), min()
print(f"최고 점수: {max(score)}점")
print(f"최저 점수: {min(score)}점")

# 성적의 총점과 평균
print(f"총점: {sum(score)}")

# 평균 점수 출력하기(평균 = 총점 / 개수)
print(f"평균: {sum(score) / len(score)}")
"""

# 사람의 키를 입력받아 최대값 찾기
def find_max(a):
    max_v = a[0] #최대값 지정
    n = len(a) #개수만큼 반복
    for i in range(n):
        if a[i] > max_v: 
            max_v = a[i]
    return max_v

number = int(input("사람수 입력: "))
# print(number)
# 사람수 만큼 반복
heights = [] #키를 저장할 빈 리스트 
for i in range(number):
    height = float(input(f"{i+1}번째 키 입력: "))
    heights.append(height)

print(f"최대값: {find_max(heights)}")