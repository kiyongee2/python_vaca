# 기본 매개변수 - 매개변수를 초기화하여 선언한 변수
# 매개변수를 생략하면 기본값으로 출력된다.
# 버스의 요금 출력 기능
def take(bus_num, fee = 1500):
    print(f"{bus_num}번 버스 요금: {fee}원")

take(101, 1700) #버스번호, 요금
take(203) #버스번호, 요금

# 문자열 반복 출력 기능
def print_string(text, count = 1):
    for i in range(count): #range(0, count)
        print(text)

# 함수 호출
print_string("banana", 3)
print_string("strawberry")

# 가변 매개변수 - 매개변수의 입력값이 정해지지 않고
# 변경해야 할때 사용하는 변수이다.(변수앞에 *을 붙임)
# 평균을 계산하는 함수 정의
def calculate(*number):
    total = 0
    for val in number:
        total += val
    return total / len(number)

result1 = calculate(1, 2, 3)
print(result1) #2.0

result2 = calculate(1, 2, 3, 4, 5)
print(result2) #3.0

# 실습 문제
# 두 수를 매개변수로 전달하여 서로 같으면 더하고,
# 서로 다르면 빼는 함수를 정의
def my_func(x, y):
    if x == y:
        return x + y
    else: # x != y
        return x - y
    
result1 = my_func(8, 8)
print("result1 =", result1) #16

result2 = my_func(8, 9)
print("result2 =", result2) #-1