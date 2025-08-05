# 숫자를 추측해서 맞히는 게임
"""
import random
'''
  1. 컴퓨터가 1 ~ 30 사이의 난수를 생성한다. 
  2. 사용자가 추측한수가 맞으면 "정답"을 출력하고
     게임이 종료됨
  3. 추측한 수가 난수보다 크면 "너무 커요!" 출력하고
     아니면 "너무 작아요!" 출력
'''
com = random.randint(1, 30)
# print(com)

while True:
    # 숫자(문자) 입력시에 숫자형으로 변환함
    you = int(input("맞혀보세요(입력: 1~30): "))
    
    if you < 1 or you > 30:
        print("범위를 초과했어요. 다시 입력하세요")
    else: #( 1 <= you <= 30)
        if you == com:
            print("정답!")
            break
        elif you > com:
            print("너무 커요!")
        else:
            print("너무 작아요")
print("프로그램 종료")
"""

