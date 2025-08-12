# 윈도우(창) 만들기
'''
   import tkinter 
   - 생성자: Tk()
   - 구성요소(컴포넌트): 프레임, 버튼, 
     라벨, 입력상자, 출력상자
   - '*'은 클래스나 함수를 의미함
'''
from tkinter import *

# 첫 윈도우 만들기
"""
def click():
    # print("안녕~ 파이썬!")
    demo.config(text="안녕~ 파이썬!")


# Tk클래스의 생성자 호출
root = Tk() #root - 인스턴스
root.title("첫 윈도우")
root.geometry("250x100+200+100")  #평면(가로x세로+x좌표+y좌표)

# 라벨(레이블)로 출력
# pack() - 한 줄을 차지함
Label(root, text="Hello~ Python!").pack()

# 버튼 생성 - <command = 함수>
# 함수괄호를 사용하면 오류 발생하므로 괄호를 생략함
Button(root, text="확인", command=click).pack()

# 확인 클릭후 메시지 출력 라벨 
demo = Label(root, text="")
demo.pack() #레이아웃(배치)이므로 생략하면 라벨이 보이지 않음

root.mainloop()
"""

# 배치 - pack() 사용
'''
   pack() - 하나의 컨트롤이 한 줄을 차지함
   # 배치
     pack(side="top") 
     - x축: left(왼쪽), right(오른쪽)
     - y축: top(위쪽), bottom(아래쪽)
   * 여백
     pack(padx=10) - 좌, 우 여백이 10픽셀
     pack(pady=10) - 상, 하 여백이 10픽셀
'''

"""
# Tk클래스의 window 인스턴스 생성
window = Tk()
window.title("pack")
window.geometry("300x200")

# 프레임 생성
frame = Frame(window)
frame.pack(side="top")  #생략하면 side="top"이다.

# 레이블
Label(frame, text="안녕하세요", font=('돋움', 12)).pack(pady=20)

# 버튼
Button(frame, text="변환", width=8).pack(side="left", padx=5)
Button(frame, text="초기화", width=8).pack(side="left", padx=5)

window.mainloop()
"""

# 배치2 - grid() 사용
'''
   Grid는 격자라는 의미이다.
   - 행과 열로 배치함
   - grid(row=0, column=0) -> 1행 1열
   - 2열 합치기 - columnspan=2
'''
window = Tk()
window.title("grid")
window.geometry("300x200")
window.option_add("*font", "돋움 12")

Label(window, text="오늘도 좋은하루 되세요").grid(row=0, column=0)
Button(window, text='동').grid(row=1, column=0, sticky=E)
Button(window, text='서').grid(row=1, column=0, sticky=W)
Button(window, text='북').grid(row=2, column=0, sticky=N) 
Button(window, text='남').grid(row=3, column=0, sticky=S)

window.mainloop()