# 달력을 표시하는 모듈 - calendar
"""
import calendar

# calendar.prcal(2025) # 전체 출력
calendar.prmonth(2025, 8) #8월

# 요일(0-월, 1-화, 2-수, 3-목, 4-금, 5-토, 6-일)
idx = calendar.weekday(2025, 8, 1) 
print(idx) #4

days = ['월', '화', '수', '목', '금', '토', '일']
print(days[0]) #월
print(days[idx] + "요일") #금요일
"""

# 날짜와 시간 관련 모듈 - datetime
import datetime

# 날짜와 시간 사용 - datetime.datetime
# 지금 현재 날짜와 시간 - datetime.datetime.today()
now = datetime.datetime.today()
print(now) #2025-08-01 15:30:03.971791

# 연, 월, 일 출력
print(now.year) #2025
print(now.month) #8
print(now.day) #1
print(f"{now.year}-{now.month}-{now.day}")

# 시, 분, 초 출력
print(now.hour)
print(now.minute)
print(now.second)
print(f"{now.hour}:{now.minute}:{now.second}")

# 현재 날짜 보기 - datetime.date
# 오늘 날짜
# today = datetime.date.today()
today = datetime.date(2025, 8, 1)
print(today) ##2025-08-01

# 특정한 날짜
the_day = datetime.date(2025, 8, 15)
print(the_day) #2025-08-15

# DDay
print("광복절까지 몇 일 남았나요(DDay)? ")
remain_day = the_day - today
print(f'광복절까지 {remain_day.days}일 남았습니다.')

# import 모듈이름
# from 모듈이름 import 모듈이름, 모듈이름
import datetime
from datetime import datetime, date
# 현재 날짜와 시간
current_time = datetime.today()
print(current_time)

# 현재 날짜
current_day = date.today()
print(current_day)











