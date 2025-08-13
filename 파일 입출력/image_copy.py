# 이미지 복사
# 파일 읽어서 쓰기

with open('fox.jpg', 'rb') as f:
    image = f.read()

with open('fox2.jpg', 'wb') as f:
    f.write(image)