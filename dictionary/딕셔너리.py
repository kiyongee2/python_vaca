# dictionary 자료구조 
# 키(key): 값(value) 형태로 구성된 자료구조임
"""
dict = {'a': 1, 'b': 2}

print(dict) #{'a': 1, 'b': 2}
print(type(dict)) #<class 'dict'>
print(dict.keys()) #dict_keys(['a', 'b'])
print(dict.values()) #dict_values([1, 2])

# 요소 추가
dict['c'] = 3
print(dict) #{'a': 1, 'b': 2, 'c': 3}

# 빈 딕셔너리 생성
person = {} 
print(person) #{}

# 요소 추가
person["name"] = "오상식"
person["age"] = 35
person["phone"] = "010-1234-5678"
print(person) # {'name': '오상식', 'age': 35, 'phone': '010-1234-5678'}

# 요소 검색 - 키(key)로 값을 검색
print(person['phone']) #'010-1234-5678'

# 요소 수정 - '오상식'을 '최지능'으로 변경
person['name'] = "최지능"
print(person)

# 요소 삭제 - pop(key) 삭제
# del person['age']
person.pop('age') 

# for문 출력
for key in person:
    print(key, ':', person[key]) #name : 최지능 phone : 010-1234-5678

print(person.keys())
print(person.values())
"""

# 응용 프로그램 - 컴퓨터 용어 사전
print("♠ 컴퓨터 용어 사전 ♠")

dic = {
    "이진수": "컴퓨터가 사용하는 0과 1로 이루어진 수",
    "알고리즘": "어떤 문제를 해결하기 위해 정해진 일련의 절차",
    "버그": "프로그램이 적절하게 동작하는데 실패하거나 \
오류가 발생하는 코드 조각"
}

while True:
    word = input("검색할 용어를 입력하세요(종료: q or Q): ")

    if word == 'q' or word == 'Q':
        print("프로그램 종료!")
        break
    else:
        if word in dic:
            definition = dic[word]
            print(definition)
        else:
            print("정의된 단어가 없습니다.")
