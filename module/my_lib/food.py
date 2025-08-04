# 모듈 직접 제작하기
def cook():
    print("요리를 합니다.")

def eat():
    print("먹는다.")

name = "장금이"

# 이름이 main이면 실행됨
# 밑줄 2개(__)를 던더라 함
if __name__ == "__main__":
    print(name)
    cook() #함수 호출
    eat()