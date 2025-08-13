# 파일 쓰기(저장)
'''
  - 파일 열기: open(파일 경로, 모드)
  - 파일 쓰기: write()
  - 파일 닫기: close()

  - 쓰기 모드: 'w'
'''

f = open("c:/pyfile/file.txt", 'w')

f.write("하늘\n")
f.write("rainy\n")
# write()는 문자만 저장할 수 있음
# f.write(128) #TypeError
#문자 포맷으로 변수에 저장하면 가능
num = 128 * 2
f.write(f'{num}') 

f.close()