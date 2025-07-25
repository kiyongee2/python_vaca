# 입력 처리 - input()

'''
print("문자 입력: ")
ch = input()  #입력 데이터 저장 변수
print("입력된 문자 : " + ch)

ch = input("문자 입력: ")
print("입력된 문자 : " + ch)
'''

# 정수 입력
"""
num = input("정수 입력: ")
print(type(num)) #str- 문자

# int(문자형) - 문자를 정수로 바꾸는 함수 
num = int(num) # '100' -> 문자형을 숫자형으로 변환
print(num + 1)
"""

# 무게의 2배 계산
"""
weight = input("무게 입력:")
weight = float(weight) #문자형을 실수형으로 변환
print(weight * 2)
"""

# 나이 계산 프로그램
# 나이(age) = 현재년도(2025) - 출생년도(birth_year) + 1

birth_year = input("출생년도 입력: ")
age = 2025 - int(birth_year) + 1

print("나이는", age, "세 입니다.")
# str(숫자) - 숫자형을 문자형으로 변환하는 함수 
print("나이는 " + str(age) + "세 입니다.")


























