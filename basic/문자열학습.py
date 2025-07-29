# 문자열 다루기
# 줄바꿈 기호 - \n
say1 = "'힘내세요!' \n라고 말했다."
print(say1)

# 홑따옴표가 겹치면 \' or \" 사용
say2 = 'No, it doesn\'t.'
print(say2)

say3 = "문자 \'12\'를 숫자 12로 변환하세요"
print(say3)

# 문자열을 여러 줄에 입력 - 쌍따옴표 or 홑따옴표 3개("""~""")
# 탭키(간격 띄기) - \t
table = """
상품명\t가격\t수량
키보드\t20000\t100
마우스\t25000\t50
모니터\t80000\t20
"""
print(table)

# 문자열 더하기와 곱하기
head = "Good"
tail = " Job!"

print(head + tail) #Good Job!
print(head * 3) #GoodGoodGood
print("==========")
print("=" * 10)


