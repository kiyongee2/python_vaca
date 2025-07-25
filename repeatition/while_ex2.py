# 반복 조건문(while ~ if ~ break)
# 1 ~ 10까지 출력
'''
n = 1
while True:
    if n > 10:
        break
    print(n)
    n += 1  #1 증가
print("===========")
'''

# 1 ~ 10까지 합계
# 1 2 3 4 ....9 10
"""
  sum = 0
  sum = sum + 1 = 0 + 1 = 1
  sum = sum + 2 = 1 + 2 = 3
  sum = sum + 3 = 3 + 3 = 6
  ...
  sum = sum + 10


n = 1
total = 0  # 합계 
while True:
    if n > 10:
        break
    total += n #total = total + n
    n += 1  #1 증가

print("합계:", total) #55
"""

# 키보드 동작 반복 
'''
  - y or Y: "계속 반복"
  - n or N: "반복 중단"
  - y or n 이외의 키: "정상 답변이 아닙니다."

'''
while True:
    key = input("계속 반복할까요(y/n 입력)? ")

    if key == 'y' or key == 'Y':
        print("계속 반복")
    elif key == 'n' or key == 'N':
        print("반복 중단")
        break
    else:
        print("정상 답변이 아닙니다.")


































