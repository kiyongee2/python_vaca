# 거북이 대포 게임
import turtle as t
import random

def turn_up():
    t.left(2)  #왼쪽으로 2도

def turn_down():
    t.right(2) #오른쪽으로 2도

def fire():
    while t.ycor() > 0: #포탄이 땅위에 있는 동안
        t.forward(15)
        t.right(5)
    
    d = t.distance(target, 0) #포탄과 목표지점과의 거리
    t.write(d)


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
