# 구구단 전체 쓰기, 읽기
# 파일 쓰기
try:
    with open('gugudan_full.txt', 'w') as f1:
        for i in range(2, 10):
            for j in range(1, 10):
                gugudan = f"{i} x {j} = {i * j}\n"
                f1.write(gugudan)
            f1.write("\n") #단별 줄바꿈
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

# 구구단 읽기
try:
    with open('gugudan_full.txt', 'r') as f2:
        gugudan = f2.read() #읽은 내용 저장
        print(gugudan)
except FileNotFoundError:
     print("파일을 찾을 수 없습니다.")