# 반복문 - while문
a = 1
print(a) #1

a += 1 #a = a + 1
print(a) #2

a += 1
print(a) #3

# "안녕" 10번 출력
n = 1  # 시작값
while n <= 10: # 종료값(식)
    print("안녕~", n)
    n += 1 # 증감값
print("-----------")

n = 10
while n > 0:
    print("안녕~", n)
    n -= 1; #n = n - 1

# 1 ~ 10까지의 합계
n = 1
total = 0
while n <= 10:
    total = total + n
    n += 1

print("합계:", total) #55




















