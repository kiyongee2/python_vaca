# random() - 난수(무작위수) 발생 함수
import random

# 범위값 - 0.0 <= x < 1.0
# print(random.random())

# a~b까지의 정수 범위 - random.randint(a, b)

# 1~3중 무작위수 발생
# print(random.randint(1, 3))

# 주사위 눈 - 1~6중 무작위수
# dice = random.randint(1, 6)
# print(dice)

# 주사위 10번 던지기
for i in range(10):
    dice = random.randint(1, 6)
    # print(dice)

# 동전 던지기
coin = random.randint(1, 2)
# print(coin)
# 1 - 앞면, 2 - 뒷면
# if(coin == 1):
#     print("앞면")
# else:
#     print("뒷면")

# 리스트에서 요소를 무작위 추출
fruits = ["strawberry", "apple", "banana"]

# print(fruits[0]) #strawberry
# print(fruits[-1]) #banana

# 랜덤 추출
fruit = random.choice(fruits)
# print(fruit)

