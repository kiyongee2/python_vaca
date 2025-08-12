# 컴퓨터 용어사전 만들기
from tkinter import *

root = Tk()
root.title("컴퓨터 용어 사전")

Label(root, text="검색할 단어를 입력하세요").grid(row=0, column=0, sticky=W)

# 입력 상자
Entry(root).grid(row=1, column=0, sticky=W)

# 버튼
Button(root, text="제출").grid(row=2, column=0, sticky=W)

# 출력 상자
Text(root, width=60, height=10).grid(row=3, column=0, sticky=W)

root.mainloop()
