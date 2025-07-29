# 리스트 자료구조에서 제공되는 주요 함수
a = [1, 2, 3]

# 4를 추가 - append()
a.append(4)
print(a) #[1, 2, 3, 4]

# 1번 위치에 5를 추가
a.insert(1, 5)
print(a) #[1, 5, 2, 3, 4]

# 맨 뒤에서 삭제 - pop()
a.pop()
print(a) #[1, 5, 2, 3]

# 0번 위치(맨 앞) 삭제
a.pop(0)
print(a) #[5, 2, 3]

# 문자형 리스트
car = ["Sonata", "BMW", "EV3"]

# 'Sportage'를 추가
car.append("Sportage")
print(car) #['Sonata', 'BMW', 'EV3', 'Sportage']

# BMW 삭제 - remove(), pop()
car.remove("BMW") 
# car.pop(1) #1번 위치 삭제
print(car)  #['Sonata', 'EV3', 'Sportage']

# 빈 리스트 선언
a2 = []
a2.append('A') # ['A']
print(a2)

a2.append('B')
print(a2) #['A', 'B']


# 리스트의 복사
arr1 = [1, 2, 3, 4, 5]
arr2 = []
arr3 = []

print("arr1 =", arr1) #arr1 = [1, 2, 3, 4, 5]
# arr1을 arr2에 복사
for val in arr1:
    arr2.append(val)

print("arr2 =", arr2) #arr2 = [1, 2, 3, 4, 5]

# arr1을 arr2에 홀수만 복사
for val in arr1:
    if val % 2 == 1:
        arr3.append(val)

print("arr3 =", arr3) #arr3 = [1, 3, 5]






