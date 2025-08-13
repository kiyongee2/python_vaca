# 컴퓨터 용어사전 만들기
"""
from tkinter import *
# 단어와 뜻을 저장할 딕셔너리 자료구조 생성
dic = {
    "이진수": "2진법으로 나타낸 숫자, 0과 1로 구성함",
    "버그": "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 \
동작하지 않는 원인을 제공하는 코드 조각",
    "함수": "특정한 기능을 수행하는 프로그램으로 재사용 가능한 코드",
    "알고리즘": "컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 \
단계별로 설명해 놓은 것"
}

# 단어 검색 함수 정의
def select():
    #try: 실행 영역, except: 오류 처리 영역 
    try:
        word = entry.get()  #입력된 단어 가져옴
        definition = dic[word] #단어로 검색한 뜻(정의) 가져옴
        # 앞 0-행(줄)을 의미, 뒤 0-첫째 문자(열), END-끝 
        output.delete(0.0, END) #정의 초기화(이전 입력을 삭제)
        output.insert(END, definition) #정의를 출력
    except KeyError:
        output.delete(0.0, END) 
        output.insert(END, "단어의 정의를 찾을 수 없습니다.")

root = Tk()
root.title("컴퓨터 용어 사전")

Label(root, text="검색할 단어를 입력하세요").grid(row=0, column=0, sticky=W)

# 입력 상자(검색창)
entry = Entry(root, width=20, bg="skyblue")
entry.grid(row=1, column=0, sticky=W)

# 버튼 (select() 함수를 연결)
Button(root, text="제출", command=select).grid(row=2, column=0, sticky=W)

# 출력 상자(단어의 뜻 출력)
output = Text(root, width=60, height=10, bg="skyblue")
output.grid(row=3, column=0, sticky=W)

root.mainloop()
"""

# 짝수/홀수 판정 프로그램
from tkinter import *

def click():
    # 숫자가 아닌 문자가 입력된 경우 예외(exception) 처리
    try:
        num = int(entry.get()) #입력상자의 값 가져옴
        output.delete(0.0, END) #이전 입력 지우기(제거)
        if num % 2 == 0:
            output.insert(END, "짝수")
        else:
            output.insert(END, "홀수")
    except ValueError:
        output.insert(END, "입력 오류")

def reset():
    entry.delete(0, END) #입력 초기화 - 한 줄(0-첫문자)
    output.delete(0.0, END) #출력 초기화 - 여러줄(0-행, 0-열)

# 윈도우 만들기
root = Tk()
root.title("짝수/홀수 판정")
root.geometry("300x150+200+200")

# 입, 출력 프레임 생성
io_frame = Frame(root)
io_frame.pack(pady=15) #배치(생략하면 화면에 보이지 않음)

# 입력
Label(io_frame, text="숫자 입력").grid(row=0, column=0)
entry = Entry(io_frame, width=15)
entry.grid(row=0, column=1)

# 출력
Label(io_frame, text="결과").grid(row=1, column=0)
output = Text(io_frame, width=15, height=1)
output.grid(row=1, column=1)

# 버튼 프레임 생성
btn_frame = Frame(root)
btn_frame.pack() #배치

# 버튼 2개 - 이벤트
Button(btn_frame, text="판정", command=click).pack(side=LEFT, padx=5)
Button(btn_frame, text="초기화", command=reset).pack(side=LEFT, padx=5)

root.mainloop()


'''
num = 13
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
'''