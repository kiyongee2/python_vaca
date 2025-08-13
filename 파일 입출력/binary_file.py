# 바이너리 파일 쓰기/읽기

# 파일 쓰기 - 쓰기모드: 'wb'
with open("data.bin", 'wb') as f:
    text = "폭우가 내려요!!"
    # encode() - 문자를 코드화함(0과 1로 변환)
    f.write(text.encode())

# 파일 읽기 - 읽기 모드: 'rb'
with open("data.bin", 'rb') as f:
    data = f.read()
    # decode() - 코드를 문자로 변환
    print(data.decode())