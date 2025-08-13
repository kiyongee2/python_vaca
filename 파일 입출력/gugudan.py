# 구구단 파일 쓰기
'''
    # 파일 경로 - 상대 경로(프로젝트 내부에 파일이 생성)
    # with 파일 as 파일 객체: 구문
      - f.close() 사용하지 않음
'''
# 구구단 쓰기
with open("gugudan.txt", 'w') as f:
    # 한 개의 단 쓰기(저장)
    dan = 7
    for i in range(1, 10):
        f.write(f"{dan} x {i} = {dan * i}\n")

# 구구단 읽기
with open("gugudan.txt", 'r') as f:
    gugu = f.read()
    print(gugu)
