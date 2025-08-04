# from 패키지(디렉터리) 이름 import 모듈이름
"""
from my_lib import food

print(food.name)
food.cook() #함수 호출
"""

# from 패키지이름.모듈이름 import 변수, 함수
from my_lib.food import name, cook, eat
from my_lib.calculator import add, sub, mul, div

# calculator.py 사용
# 더하기
value1 = add(10, 4)
print(value1)

# 빼기
value2 = sub(10, 4)
print(value2)

# 곱하기
value3 = mul(10, 4)
print(value3)

# 나누기
# value4 = div(10, 4)
value4 = div(10, 0)
print(value4)

# food.py 사용
# print(name)
# cook()
# eat()