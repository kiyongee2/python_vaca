# 리스트를 파일에 쓰기

# 리스트
cartlist = ["달걀", "라면", "콜라", "바나나"]

try:
    # 파일 열기
    f = open("c:/pyfile/cartlist.txt", 'w')

    # 파일 쓰기
    for cart in cartlist:
        f.write(cart + " ")

    # 파일 닫기
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")