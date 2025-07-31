# 함수(function) - 특정 기능을 수행하는 코드 블럭
# def 함수이름(): , 사용 - 함수이름을 호출
# return이 없는 함수 정의
"""
def say_hello():
    print("안녕하세요~")

def say_hello2(name): #name - 매개변수(파라미터-parameter)
    print(name + "님 안녕하세요~") #name = "영우"

def print_gugu(dan): #dan = 6
    for i in range(1, 10):
        # print(dan, 'x', i, '=', (dan*i))
        print(f"{dan} x {i} = {dan*i}")

# 함수 호출   
say_hello()
say_hello2("영우")
say_hello2("임시연")

# 구구단 호출
print_gugu(6)
"""

# return이 있는 함수
# 제곱수를 구하는 함수
def get_square(x): #x=4
    return x * x

# 절대값을 구하는 함수
# 어떤수가 음수이면 양수로 바꾸고, 양수는 양수를 유지
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x
    
# 응원의 메시지를 출력하는 함수
def message():
    return "Good Luck!"

# 제곱수 함수 호출 - 반환값을 받음
value1 = get_square(10)
print("제곱수:", value1)

# 절대값 함수 호출
value2 = my_abs(-3)  
print("절대값:", value2)

# 메시지 출력 함수
msg = message()
print(msg)