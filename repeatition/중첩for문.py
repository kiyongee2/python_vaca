# 5행 5열 공간에 출력
for i in range(1, 6):
    for j in range(1, 6):
        print("가", end='')
    print()

# 5행 5열 이차원 공간 - 숫자 채우기
# i - 행(row), j - 열(column)
# 23까지 출력
for i in range(0, 5):
    for j in range(1, 6):
        # 5는 칼럼(column)의 종료값
        num = i * 5 + j
        if num > 23:
            break  #for문 탈출
        print(num, end=' ')
    print()

# 응용 프로그램 - 자리 배치도
'''
  - 입장객수, 좌석 열수
    1. 좌석열수로 입장객수가 나누어 떨어지는 경우
    2. 좌석열수로 입장객수가 나누어 떨어지는 않는 경우
       (줄이 1개 더 필요하다.)
    3. 나머지 연산자(%) 사용
    4. 몫 연산자(//)

'''
customer = int(input("입장객 수 입력: "))
column = int(input("좌석 열수 입력: "))

if customer % column == 0:
    row = customer // column  #몫
else:
    # 나누기하면 실수이므로 정수로 변환함
    row = int(customer / column) + 1

# print(f"{row}개의 줄이 필요합니다.")
for i in range(0, row):
    for j in range(1, column + 1):
        seat_num = i * column + j
        # 좌석번호가 입장객수가 많으면 반복 종료
        if seat_num > customer:  
            break
        print(seat_num, end=' ')
    print()

