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

# 영어 타자 게임
import random
import time

'''
  1. 게임이 시작되면 영어 단어가 화면에 표시된다.
  2. 사용자가 빠르고 정확하게 입력한다.
  3. 단어가 일치하면 "통과"를 출력하고,
     오타면 "오타! 다시 도전!"이 출력되고, 문제가 다시 출제됨

'''

words = ["sky", "earth", "sun", "moon", "flower",
    "tree", "mountain", "strawberry", "garlic", "potato"]
# print(len(words)) #10
n = 1 #문제 번호

print("[타자 게임] 준비되면 엔터>> ")
input()

start = time.time() # 시작 시간
while n <= 10:
    print("문제", n)
    word = random.choice(words)
    print(word) #문제 출제

    you = input() #사용자 답을 입력
    if you == word:
        print("통과!")
        n += 1  #다음 문제로 증가
    else:
        print("오타! 다시 도전!")
end = time.time() #종료 시간
et = end - start  #게임 소요시간 

print(f"게임 소요 시간: {et:.2f}초")