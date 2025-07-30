# 리스트의 주요 함수
# 숫자를 저장하는 정수형 리스트 생성
n = [1, 4, 3, 2]
n.sort() # 정렬(오름차순)
print(n) # [1, 2, 3, 4]

n.reverse() # 뒤집기
print(n) # [4, 3, 2, 1] 

# 문자형 리스트 생성
lower = ['b', 'c', 'a', 'd']
lower.sort()

# 아스키 코드값
# 'a'-97, 'b'-98, 'c'-99, 'd'-100
print(lower) #['a', 'b', 'c', 'd']

lower.reverse()
print(lower) #['d', 'c', 'b', 'a']

# 리스트에 여러개의 요소 추가 - extend()
v = ['a', 'b']
# 'c' 추가
v.append('c') #['a', 'b', 'c']  
print(v)

# 'd', 'e' -> 두 개의 요소 추가
v.extend(['d', 'e']) 
print(v) #['a', 'b', 'c', 'd', 'e']

# 리스트 복사
m = [1, 2, 3]
n1 = [] #빈 리스트
n2 = [] #빈 리스트

# m 리스트를 n1 리스트로 복사 
for val in m:
    n1.append(val)
print(n1) #[1, 2, 3]

# 리스트 복사 - copy()
n2 = m.copy()
print(n2)  #[1, 2, 3]

n2[1] = 4
print(n2) #[1, 4, 3]


