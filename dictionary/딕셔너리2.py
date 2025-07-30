# 딕셔너리 생성
dic ={1:'a', 2:'b', 3:'c'}
print(dic) #{1: 'a', 2: 'b', 3: 'c'}
print(dic.keys()) #dict_keys([1, 2, 3])
print(dic.values()) #dict_values(['a', 'b', 'c'])

# 인덱싱(조회) - 키로 값을 검색
print(dic[2]) #'b'

# 요소 추가 - 4:d
dic[4] = 'd'
print(dic) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 요소 수정 - 'c'를 'e'로 변경
dic[3] = 'e'

# 요소 삭제 - 2번 삭제
dic.pop(2)

# 전체 요소 검색
for key in dic:
    print(key, ':', dic[key])

# 연습 문제
member = {"이름": "신유빈", "나이":20, "특기": "탁구"}
result = member.pop("나이") #pop("키값")
# del member["나이"]  #즉시 실행(삭제)

print(member) #{'이름': '신유빈', '특기': '탁구'}
print(result) #20


