# turtle.goto(x, y) -> 좌표 이동
import turtle as t

t.shape("turtle")
#속도- 1~10이 있고 10이 빠름
# 0이 가장 빠른 속도임
# t.speed(0) 
# t.goto(200, 0) # x=200, y=0
# t.goto(0, 200) # x=0, y=200

# 직선 그리기
'''
t.goto(-200, 0)
t.goto(200, 0)
'''

import turtle as t
import time
# 사각형 그리기
# 좌표(0, 0)에서 시작
# 1초 시간 대기 - time.sleep(1)
"""
t.goto(0, 0) #출발점

time.sleep(1)
t.goto(-100, 0)

time.sleep(1)
t.goto(-100, -100)

time.sleep(1)
t.goto(0, -100)

time.sleep(1)
t.goto(0, 0) #출발점

time.sleep(1)
t.goto(0, 100)

time.sleep(1)
t.goto(100, 100)

time.sleep(1)
t.goto(100, 0)

time.sleep(1)
t.goto(0, 0)
"""

# 랜덤 위치로 가기
import random
# stage(무대) - 500(w) x 500(h)
'''
x = random.randint(-250, 250)
y = random.randint(-250, 250)
t.up()  #선 그리지 않음
print("x=", x, ", y=", y)
t.goto(x, y)
'''

# 마음대로 걷는 거북이
# 거북이 머리 방향(각도) - 난수
# t.setheading(0) #오른쪽
# t.setheading(90) #위쪽
t.speed(0)
n = 300
for i in range(n):
    ang = random.randint(1, 360)
    t.setheading(ang)
    t.forward(20)

t.mainloop()