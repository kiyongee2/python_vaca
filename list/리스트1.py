season = "여름"
print(season)

# 리스트 - 여러개의 자료를 저장하는 자료구조
seasons = ["봄", "여름", "가을", "겨울"]

# 특정 요소 접근(검색) - 인덱싱(0번부터 시작 끝은 -1)
print(seasons[0]) #봄
print(seasons[1]) #여름
print(seasons[-1]) #겨울

# in 연산자 (~안에 유무 확인)
print("가을" in seasons) # True
print("winter" in seasons) # False

# 리스트의 개수 - len()
n = len(seasons)
print(n) #4

# 전체 요소(값) 출력1
for i in range(0, n): #0, 1, 2, 3
    print(seasons[i])

# 출력2 (for i in 리스트이름)
for item in seasons:
    print(item)

# 음식 분류 - 한식, 일식, 중식
# 리스트는 순서가 있고, 요소의 중복이 가능하다.
foods = ["비빔밥", "자장면", "초밥", "김치찌게", "초밥"]
print(type(foods)) #<class 'list'>
print(foods) #['비빔밥', '자장면', '초밥', '김치찌게', '초밥']
print(len(foods))
print(foods[-1]) #초밥
print(foods[-2]) #김치찌게

for food in foods:
    if food in ['자장면', '짬뽕', '탕수육']:
        print(f"{food}는(은) 중식입니다.")
    elif food in ["초밥", "우동"]:
        print(f"{food}는(은) 일식입니다.")
    else:
        print(f"{food}는(은) 한식입니다.")


