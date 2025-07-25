# 반복문(for문) - for ~ in range()
# range(시작값, 종료값, 증감값)
# 시작값은 0부터 시작함
# 종료값은 실제 종료값-1이 출력됨
'''
print(range(1, 10, 1))
print(list(range(1, 10, 1))) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

"""
# 1 ~ 10 까지 출력하기
for n in range(1, 11, 1):
    print(n, end=' ')
print() #줄바꿈

# 1 ~ 10중에 홀수만 출력
for n in range(1, 11, 2):
    print(n, end=' ') #1 3 5 7 9
print()

for n in range(1, 11):
    if n % 2 == 1:
        print(n, end=' ') #1 3 5 7 9
print()

# 1 ~ 30 중에 3의 배수 출력
# 3의 배수의 개수
count = 0 #개수를 저장하는 변수
sum_v = 0 #합계
for n in range(1, 31):
    if n % 3 == 0:
        count += 1
        sum_v += n
        print(n, end=' ') #3 6 9 12 15 18 21 24 27 30

# 평균 = 합계 / 개수
average = sum_v / count

print()     
print("개수:", count) # 10
print("합계:", sum_v) # 165
print("평균:", average) # 16.5
"""

# 구구단 출력하기
# int(문자) : 문자를 숫자로 변환 
dan = int(input("단 입력: "))

for i in range(1, 10, 1):
    print(dan, 'x', i, '=', (dan * i))


# 문자 더하기
'''
print("가" * 3)
print("-" * 20)
'''























        




