# 거북이 대포 게임
import turtle as t
import random

def turn_up():
    t.left(2)  #왼쪽으로 2도

def turn_down():
    t.right(2) #오른쪽으로 2도

def fire():
    ang = t.heading() #거북이가 바라보는 현재 각도
    while t.ycor() > 0: #포탄이 땅위에 있는 동안
        t.forward(15)
        t.right(5)
    
    d = t.distance(target, 0) #포탄과 목표지점과의 거리
    # t.write(d) #거리값 출력
    t.sety(random.randint(10, 100)) #y좌표 - 성공, 실패를 표시할 위치
    if d < 25: #목표 지점에 닿으면 
        t.color('blue')
        #False- 거북이 위치를 옮기지 않음. center-문자 가운데 정렬, 글자크기-17
        t.write("Good!", False, 'center', ('', 17))
    else: #목표 지점에 닿지 않으면
        t.color('red')
        t.write("Bad!", False, 'center', ('', 15))
        t.color('black')
        t.goto(-200, 10) #거북이를 처음 발사위치로 보냄
        t.setheading(ang) #처음 기억한 각도로 되돌림

# 땅 그리기
t.goto(-300, 0)
t.goto(300, 0)

# 목표 지점 설정
target = random.randint(50, 150)
t.color('green')
t.pensize(2)
t.up()  #펜 올리기

# 목표 지점의 크기 - 50px
t.goto(target-25, 1)  #x좌표 최소 25, y좌표 1
t.down() #펜 내리기
t.goto(target+25, 1)  #x좌표 최소 75, y좌표 1

# 포탄의 처음 위치
t.color('black')
t.up()
t.goto(-200, 10) # 처음 위치
t.setheading(20) #화살촉(포탄)의 각도

# 거북이 대포 동작 설정
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
# 스페이스 키를 누르면 발사
t.onkeypress(fire, "space") 
t.listen() # 동작 실행 

t.mainloop()
