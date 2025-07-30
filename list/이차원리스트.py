# 2차원 리스트 
# 데이터 관리 - 생성, 조회(검색), 수정, 삭제
d = [
    [10, 20],
    [30, 40],
    [50, 60]
]
print(d) #[[10, 20]]
print(type(d)) #<class 'list'>

# 행 출력
print(d[0]) #[10, 20]
print(d[1]) #[30, 40]

# 요소(값) 출력
print(d[0][1]) #20
print(d[1][0]) #30

# 리스트의 크기
print("행의 크기:", len(d)) #3 -> 3행
print("열의 크기:", len(d[0])) #2 -> 2열
print("열의 크기:", len(d[1])) #2 -> 2열

# 전체 출력 - range()
for i in range(len(d)):  #range(0, len(d))
    for j in range(len(d[i])):
        print(d[i][j], end=' ')
    print() # 행 바꿈
print('----------------')

# 행 단위로 출력
for row in d:
    print(row)

# 특정 열 출력
for row in d:
    print(row[0])

# 전체 출력 - 리스트 이름
for row in d: #행 순회
    for val in row: #열 순회
        print(val, end=' ')
    print()

# 리스트 추가
d.append([70, 80]) 
print(d)
"""
#[
  [10, 20], 
  [30, 40], 
  [50, 60], 
  [70, 80]
]
"""
# 특정 요소값 수정 - 40을 100으로 변경
d[1][1] = 100
print(d)

# 특정 리스트 삭제 - [50, 60]
del d[2]
print(d) #[[10, 20], [30, 100], [70, 80]]

# 특정 열삭제
for row in d:
    del row[0]
print(d) #[[20], [100], [80]]

# d 리스트 삭제
d.clear()
print(d) #[]
