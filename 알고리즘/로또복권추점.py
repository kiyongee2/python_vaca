#로또 복권 추첨 프로그램
'''
  - 1 ~ 45까지 자연수를 사용
  - 6개 번호를 난수로 추첨
  - 중복을 허용하지 않음
'''
import random

# 로또번호 1개 추첨
# lotto = random.randint(1, 45)
# print(lotto)

lotto = []  #6개의 번호를 저장할 리스트
'''
for i in range(6):
    num = random.randint(1, 45) #랜덤한 번호
    if num not in lotto: #로또 리스트에 없는 번호를 저장
        lotto.append(num)
'''
# while 사용
while len(lotto) < 6: #번호가 6개 될때까지 반복
    num = random.randint(1, 45) #랜덤한 번호
    if num not in lotto: #로또 리스트에 없는 번호를 저장
        lotto.append(num)

print(lotto)
# 오름차순 정렬 함수 - sorted
print(sorted(lotto)) #[3, 7, 15, 19, 21, 32]  