# 리스트 자료구조 - 여러 개의 연속적인 값을 저장하는 자료 구조 
cart = "라면"  #문자 저장 변수
print(cart)

# 리스트 생성
carts = ["라면", "달걀", "콩나물", "쌀"]

# 리스트의 개수
print("리스트의 개수:", len(carts))

# 인덱스(위치)로 검색
print(carts[0]) #라면
print(carts[3]) #쌀
print(carts[-1]) #쌀

# 리스트 요소 전체 출력
print(carts) #['라면', '달걀', '콩나물', '쌀']

# in 연산자(예약어) 
print("달걀" in carts) # True
print("콜라" in carts) # False
print("콩나물" not in carts) # False

# 요소 수정 - "쌀을 빵으로 수정"
carts[-1] = "빵"

# for i in 리스트이름:
for i in carts:
    print(i)
