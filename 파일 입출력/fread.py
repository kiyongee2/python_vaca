# 파일 읽기
'''
  - 파일 열기: open(파일 경로, 모드)
  - 파일 읽기: read()
  - 파일 닫기: close()

  - 읽기 모드: 'r'
'''

f = open("c:/pyfile/file.txt", 'r')

data = f.read() #파일에서 읽은 데이터 저장
print(data)
