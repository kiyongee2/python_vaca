# 모듈(module) - 변수나 함수 또는 클래스를 모아놓은 소스 파일이다.
# 모듈을 사용하려면 [import 모듈이름]을 선언한다.
# 수학 관련 모듈 - math
import math

# 반올림
value1 = round(128.93, 1)
print(value1) #128.9

# 내림(버림)
value2 = math.floor(2.54)
print(value2) #2

# 올림
value3 = math.ceil(1.309) 
print(value3) #2

# 제곱근
print(math.sqrt(2)) #1.4142135623730951  
print(math.sqrt(36)) #6

# 거듭제곱
print(pow(3, 3)) #27

# 원주율 상수 - math.pi
print(math.pi) #3.141592653589793
# 원의 넓이 = math.pi * 반지름 * 반지름 
radius = 4
area = math.pi * radius * radius 
print(f'원의 넓이: {area:.2f}') #50.27 

