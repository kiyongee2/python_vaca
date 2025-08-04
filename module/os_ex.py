'''
 * os 모듈
 - 환경변수나 디렉터리, 파일등의 OS 자원을 제어할 
   수 있게 해주는 모듈이다.
'''

import os
# pyworks 디렉터리(폴더)로 이동
os.chdir("c:/pyworks")

# 목록 보기
dir = os.popen("dir")
print(dir.read())