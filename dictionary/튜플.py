# 튜플(tuple) - 어떤 자료를 수정, 삭제를 못하게하는 자료구조
# 소괄호 사용
# 튜플 생성
t = (1, 2, 3)
print(t) #(1, 2, 3)
print(type(t)) #<class 'tuple'>

# 조회(인덱싱)
print(t[0])  #1
print(t[1])  #2
print(t[-1]) #3

# 조회(범위-슬라이싱)
print(t[0:3]) #(1, 2, 3)
print(t[:]) #(1, 2, 3)
print(t[0:-1])  #(1, 2)

# 수정 불가
# t[0] = 4

# 삭제 불가
# del t[1]

# 튜플의 요소를 1개 생성할때는 뒤에 콤머(,)를 반드시 붙임
t2 = (10, )
print(t2) #(10,)
print(type(t2)) #<class 'tuple'>

# tuple 합치기
t3 = t + t2
print(t3) #(1, 2, 3, 10)

# 문자를 저장한 튜플
tu = ('s', 'k', 'y')
print(tu)

print(tu[1]) #'k'
print(tu[:]) # ('s', 'k', 'y')