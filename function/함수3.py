# 사각형의 면적을 계산하는 프로그램
# 사각형의 넓이(area) = 가로(width) x 세로(height)
# 함수 정의
def rectangle(w, h):
    area = w * h
    return area

# 삼각형의 넓이(area) = 밑변(size) x 높이(height) / 2
def triangle(s, h):
    area = s * h / 2 
    return area

result1 = rectangle(4, 5) #함수 호출
print("사각형의 넓이:", result1)
print(type(result1)) #<class 'int'>

result2 = triangle(5, 8) #20
print("삼각형의 넓이:", result2) # 20.0 
print(type(result2)) # <class 'float'>

# 구조 할당(변수, 튜플)
# a = 10
# b = 20
# print(a, b)

a, b = 10, 20
print("a =", a)
print("b =", b)

# 튜플 - 구조 할당
x, y = (10, 20)
print("x =", x)
print("y =", y)

# return 반환값 - 여러 개인 경우
def add_and_mul(a, b):
    return a+b, a*b

value1 = add_and_mul(10, 4)
print(value1)  #(14, 40)
print(type(value1)) #<class 'tuple'>

# 구조 할당
add, mul = value1
print(add) #14
print(mul) #40