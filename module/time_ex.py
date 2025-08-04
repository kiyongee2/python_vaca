# time(시간) 모듈
import time
from datetime import datetime

# 1970. 1. 1 자정이후 시간이 시작됨
# 컴퓨터 운영체제 - 유닉스 개시일
# time.time() - 현재시간을 실수형태로 반환하는 함수
second = round(time.time())
print(f'{second}초') #1754280345초
day = round(time.time() / (24*60*60))
print(f'{day}일') #20304일
year = round(time.time() / (365*24*60*60))
print(f'{year}년') #56년

# 날짜와 시간 내역
print(time.localtime())
# 현재 날짜와 시간
print(time.ctime()) #Mon Aug  4 13:16:26 2025
print(datetime.today()) #2025-08-04 13:18:04.072081

# 시간 측정 - 수행 시간
# 1부터 n까지 출력
start = time.time() # 시작 시간

n = 100
for i in range(1, n + 1):
    print(i)
    time.sleep(0.1)  #0.5초 대기

end = time.time()
print(f"수행시간: {(end - start):.3f}초")