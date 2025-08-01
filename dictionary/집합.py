# 집합(set) 자료구조
# 중복이 허용되지 않음.
# 생성
s1 = {1, 2, 3, 1, 2}
print(s1) #{1, 2, 3}
print(type(s1)) #<class 'set'>

# 순서가 없어서 인덱싱(위치 검색) 안됨
s2 = {'s', 'k', 'y'}
print(s2) #{'k', 's', 'y'}
# print(s2[0]) #TypeError: 

s3 = set() #빈 집합 생성
print(s3) #set()

# 요소 추가
s3.add('a')
s3.add('p')
s3.add('p')
s3.add('l')
s3.add('e')
print(s3) #{'a', 'p', 'l', 'e'} 

# 요소 검색 - 불가
# print(s3[-1])

# 요소 수정 - 불가
# s3[0] = 'b'

# 요소 삭제
s3.remove('a')
print(s3) #{'e', 'l', 'p'}

# set 생성
fruits = {"apple", "grape", "banana"}

# 요소 추가
fruits.add("peach")
print(fruits) #{'grape', 'peach', 'apple', 'banana'}

# 요소가 있는지 여부 - True/False
print("banana" in fruits) #True
print("strawberry" in fruits) #False
print("grape" not in fruits) #False

# "apple" 삭제하기
fruits.remove("apple")
print(fruits)