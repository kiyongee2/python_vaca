# 영어 타자 게임
import random
import time
import os

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

os.system("pause")  #콘솔창이 자동으로 닫히지 않음