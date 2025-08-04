# 간단한 계산기 프로그램
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    # 분모가 0이 아니면 나누기 실행
    # 분모가 0이면 "0으로 나눌수 없슴"
    if y != 0:
        return x / y
    else:
        print("0으로 나눌수 없습니다.")