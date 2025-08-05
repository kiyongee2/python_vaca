# 거북이 모듈 - 이동
import turtle

turtle.shape("turtle")  #거북이 모양

"""
# 사각형 그리기
turtle.forward(100) #직진 100픽셀 이동
turtle.right(90)  #오른쪽으로 90도 회전
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100) 
turtle.right(90)

# 삼각형 그리기
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
"""

"""
# 사각형 - 반복문
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# 삼각형 - 반복문
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
"""

# 변수 사용하기
d = 60  #거리
n = 4    #반복 횟수

# 사각형
for i in range(n):
    turtle.forward(100)
    turtle.left(360/n) #360/4=90

# 삼각형
n = 3
for i in range(n):
    turtle.forward(100)
    turtle.right(360/n) #360/3=120

turtle.mainloop() #실행창 유지