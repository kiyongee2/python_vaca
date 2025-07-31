# 변수의 유효 범위(scope)
"""
  - 전역변수는 메인영역에 위치, 함수나 제어문의 변수값을 공유합니다.
    프로그램이 종료되면 메모리에서 소멸(삭제)함.
  - 지역변수는 함수나 제어문의 블럭안에서 생성되고
    호출된 후 값을 반환하고 메모리에서 소멸함
  - 정적변수는 지역변수에 global 키워드를 붙여서
    전역변수화 함.
"""
'''
def get_price():
    # 지역 변수(local variable) - price
    price = 2000 * quantity # 가격 = 금액 x 수량
    print(f"{quantity}개에 {price}원 입니다.")

quantity = 2  #수량, 전역 변수(global variable)
get_price() 

print("전역변수:", quantity)
# print("지역변수:", price) #이미 소멸되어서 오류 발생
'''
def click():
    # x = 0   # 지역 변수
    global x  # 정적 변수 - 지역변수가 전역변수화 함
    x = x + 1
    print(f"x = {x}")

x = 0  #전역 변수

click()
click()
click()