# 파일에서 리스트(문자열) 읽기
import random
# 파일 열기
try:
    f = open("c:/pyfile/cartlist.txt", 'r')

    # 파일 읽기
    '''
    data = f.read() 
    print(data) #문자열
    '''
    # 문자열 분리 - 리스트로 변환됨
    carts = f.read().split() #공백문자 분리
    print(carts) #['달걀', '라면', '콜라', '바나나']

    # 문자열 랜덤하게 출력
    cart = random.choice(carts)
    print(cart)

    # 파일 닫기
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

