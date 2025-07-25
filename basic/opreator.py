#연산자(operator) - 산술연산, 대입연산, 비교연산, 논리연산, 비트 연산
# 산술 연산자 - (+, -, *, /)
'''
n1 = 10
n2 = 4

print(n1 + n2)  #14
print(n1 - n2)  #6
print(n1 * n2)  #40
print(n1 / n2)  #2.5 - 나누기
print(n1 // n2) #2 - 몫
print(n1 % n2)  #2 - 나머지
print(n1 ** n2) #10000 - 10의 4제곱(거듭제곱)

# 대입 연산자 - '='
user_id = "smile"
password = "k1234"

print("user_id =", user_id)
print("user_id = " + user_id) #'+' 문자 연결

print("password =", password)
print("password = " + password)

# 변수값 교환하기 - swap
x = 1
y = 2

print("===== 교환 전 =====")
print("x =", x, ", y =", y)
'''

# 교환 코드 작성
# temp - 임시변수 사용
'''
temp = x
x = y
y = temp


# 직접 교환(구조 할당 방식)
# x, y = 10, 20 -> x = 10, y = 20
x, y = y, x

print("===== 교환 후 =====")
print("x =", x, ", y =", y)
'''

# 복합 대입 연산자- 산술 + 대입
"""
val = 20

val += 2  #val = val + 2
print(val) #22

val -= 2 #val = val - 2
print(val) #20

val *= 2 #val = val * 2
print(val) #40

val /= 2 #val = val / 2
print(val) #20.0(실수)
"""

# 자료형 변환(type conversion)
# int(문자) - 숫자로 변환
# str(숫자) - 문자로 변환
'''
val_1 = "123"
val_1 = int(val_1)
print(val_1 + 100) #223

# 실수를 정수로 변환
val_2 = 3.14
val_2 = int(val_2) 
print(val_2) #3

# 숫자를 문자로 변환
val_3 = 123
print(str(val_3)) #'123'

# 정수를 실수로 변환
val_4 = 21
val_4 = float(val_4)
print(val_4) #21.0
'''

# 비교 연산자
x = 10
y = -10

print(x > 0) # True
print(y > 0) # False

print(x > y)  # True
print(x < y)  # False

print(x == 10) # True
print(x == y) # False
print(x != y) # True

print(x is y) # False
print(x is not y) #True


# 논리 연산자 - and, or, not
# and - 두 조건이 모두 참일 때 참
# or - 두 조건중 하나만 참이어도 참
# not - 조건이 참이면 거짓, 거짓이면 참 
print(x > 0 and y > 0) # True and False -> False
print(x > 0 or y > 0)  # True or False -> True
print(not (y > 0)) # not False -> True












































