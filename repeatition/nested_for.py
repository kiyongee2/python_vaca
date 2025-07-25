# 중첩 for(이중 for문)
# 바같쪽(행-row), 안쪽(열-column)
# 행은 줄바꿈을 해야함 
for i in range(1, 6):
    for j in range(1, 6):
        print('*', end = '')
    print()

'''
   i=1, j=1, *
        j=2, **
        j=3, ***
        j=4, ****
        j=5, *****
        j=6, 반복종료
   i=2, j=1, *
        j=2, **
        j=3, ***
        j=4, ****
        j=5, *****
        j=6, 반복종료
   ...
   i=6, 반복 종료

   *
   **
   ***
   ****
   *****
   1행 - 1(별 - 열의 종료)
   2행 - 2
   3행 - 3
   4행 - 4
   5행 - 5

   *****
   ****
   ***
   **
   *
'''
"""
# 삼각형 모양 - 별찍기
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end = '')
    print()
print()

# 역 직각삼각형
for i in range(1, 6):
    for j in range(1, 7-i):
        print('*', end = '')
    print()
print()
"""

# 구구단 전체 출력
for i in range(2, 10):
    print('[', i, '단]')
    for j in range(1, 10):
        print(i, 'x', j, '=', (i * j))
    print()


# 구구단을 단보다 곱하는 수가 작거나 같은 경우까지 출력
# 방법1
for i in range(2, 10):
    print('[', i, '단]')
    for j in range(1, i + 1):
        print(i, 'x', j, '=', (i * j))
    print()

# 방법 2
for i in range(2, 10):
    print('[', i, '단]')
    for j in range(1, 10):
        if i >= j:
            print(i, 'x', j, '=', (i * j))
    print()














