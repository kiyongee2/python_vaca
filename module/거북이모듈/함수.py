# 다각형 그리기
"""
import turtle as t  #as(alias - 별명)

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n, d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)

polygon(3)  #삼각형
polygon(5)  #오각형

t.up() #펜 올리기(선 출력이 안됨)
t.forward(100)
t.down() #펜 내리기(선 출력됨)

polygon2(3, 100) #삼각형
polygon2(5, 100)  #오각형

t.mainloop()  #계속 실행
"""

# 키보드로 거북이 조종하기
import turtle as t

t.shape("turtle")

# 오른쪽으로 회전
def turn_right():
    t.setheading(0) #머리방향 - 오른쪽
    t.forward(10)

# 위쪽으로 회전
def turn_up():
    t.setheading(90) #머리방향 - 위쪽
    t.forward(10)

# 왼쪽으로 회전
def turn_left():
    t.setheading(180) #머리방향 - 왼쪽
    t.forward(10)

# 아래쪽으로 회전
def turn_down():
    t.setheading(270) #머리방향 - 아래쪽
    t.forward(10)

# 키보드 동작
# Right - 상수, 첫글자 대문자, 
t.onkeypress(turn_right, "Right") #오른쪽 화살키
t.onkeypress(turn_up, "Up")     #위쪽 화살키
t.onkeypress(turn_left, "Left") #왼쪽 화살키
t.onkeypress(turn_down, "Down") #아래쪽 화살키
t.listen() #동작 실행

t.mainloop()