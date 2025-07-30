# 문자열 함수
# split(구분기호) : 문자열을 리스트로 변환
fruit = "banana grape kiwi"
print(fruit) #banana grape kiwi
print(type(fruit)) #<class 'str'>  

fruit = fruit.split(' ') #공백문자로 구분
print(fruit) #['banana', 'grape', 'kiwi']

# 인덱싱(위치로 조회)
print(fruit[0]) #banana
print(fruit[-1]) #kiwi

# 요소 전체 출력
for item in fruit:
    print(item)

# replace(old, new) - 문자열 변경
s = "Hello, World"
s = s.replace("World", "Korea")
print(s) #Hello, Korea

# find(문자) - 문자의 위치(인덱스번호)
print(s.find('H')) #0
print(s.find("Korea")) #7
print(s.find('s')) #-1

title = "점프 투 파이썬"
if title.find("파이썬") != -1:
    print("파이썬과 관련된 책이군요!")
else:
    print("파이썬과 관련된 책이 아니군요!")

# strip() - 공백 문자 제거
say1 = "   Hi~ han."
print(say1)
# say = say.strip() #양쪽 모두 제거
say1 = say1.lstrip() #왼쪽만 제거
print(say1)

say2 = "Hi~ lee.  "
say2 = say2.rstrip() #오른쪽 제거
print(say2)