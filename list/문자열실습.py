# 문자열 - 1차원 리스트
f1 = ['a', 'p', 'p', 'l', 'e']
print(f1[0]) #a
print(f1[-1]) #e

f2 = "apple"
print(f2[0]) #a
print(f2[-1]) #e

# 범위를 추출 - 슬라이싱[시작:종료], ':' - 범위 연산자
# 추출된 값은 인덱스(종료-1)
say = "Have a nice day!"

print(say[0]) #H
print(say[-1]) #!
print(say[0:4]) #Have

# nice 추출하기
print(say[7:11]) # nice

s1 = "20250729Hot"
year = s1[:4] #[0:4]
print(year)

day = s1[4:8]
print(day) #0729

weather = s1[8:] #Hot
print(weather)

# in 연산자 
animals = "dog cot horse"
print('dog' in animals) #True
print('cat' in animals) #False

# 응용 프로그램 - 챗봇
# 단어가 포함되어 있으면 문장을 완성해주는 프로그램
"""
while True:
    user_input = input("사용자(exit 입력시 종료): ")

    if user_input == "exit":
        print("챗봇: 대화를 종료합니다. 안녕히 가세요.")
        break
    else:
        if "안녕" in user_input:
            print("챗봇: 안녕하세요! 방가와요!")
        elif "이름" in user_input:
            print("챗봇: 저는 Python 챗봇입니다.")
        elif "날씨" in user_input:
            print("챗봇: 날씨앱을 이용해 주세요")
        else:
            print("챗봇: 죄송해요. 잘 이해하지 못했어요")
"""

# 민생 회복 소비 쿠폰 신청
birth_year = input("출생연도 입력: ")

length = len(birth_year)
# print(length)

if length != 4:
  print("입력 오류: 출생연도는 4자리여야 합니다.")
else:
  # birth_year[3] 또는 birth_year[-1] 모두 맞음
  if birth_year[-1] == '1' or birth_year[-1] == '6':
    print("신청일은 월요일입니다.")
  elif birth_year[-1] == '2' or birth_year[-1] == '7':
    print("신청일은 화요일입니다.")
  elif birth_year[-1] == '3' or birth_year[-1] == '8':
    print("신청일은 수요일입니다.")
  elif birth_year[-1] == '4' or birth_year[-1] == '9':
    print("신청일은 목요일입니다.")
  elif birth_year[-1] == '5' or birth_year[-1] == '0':
    print("신청일은 금요일입니다.")
  else:
    print("신청요일이 아닙니다.")