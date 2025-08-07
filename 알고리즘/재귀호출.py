# 재귀 호출 알고리즘
'''
  재귀 함수(recursive function)
  - 어떤 함수안에서 자기 자신을 부르는 것
  - 재귀 호출은 무한 반복하므로 종료 조건이 필요함
    if 입력값이 충분히 작으면(종료)
       return 결과값
    else # 더 작은값으로 호출
       return 결과값
'''
# 조난 신호 보내기
"""
def sos(n):
    if n <= 0:
        return '' #빈 문자열 리턴
    else:
        print("Help me!")
        return sos(n-1) #더 작은값으로 호출

    '''
    print("Help me!")
    n = n - 1
    if n > 0:
        sos(n)
    '''
# sos(1)
sos(3)
"""

# 팩토리얼을 구하는 재귀함수
'''
  1부터 5까지 곱하기
  1 x 2 x 3 x 4 x 5 = 120
  5! = 5 x 4 x 3 x 2 x 1
  5! = 5 x 4!
  4! = 4 x 3!
  3! = 3 x 2!
  2! = 2 x 1!
  1! = 1 x 1
  시간 복잡도(빅 O)

'''
# 팩토리얼 알고리즘 - O(n)
def factorial(n):
    if n <= 1:
        return 1 # 종료값 1 반환
    else:
        # 자신을 호출하면서 좀 더 작은값으로 호출
        return n * factorial(n - 1)
    
# 곱셈 알고리즘 - O(n)
def gobN(n):
    gob = 1  #곱한 결과값
    for i in range(1, n + 1):
        gob *= i #gob = gob * i
    return gob
'''
  n=4 일때
  i=1, 1 * 1 = 1
  i=2, 1 * 2 = 2
  i=3, 2 * 3 = 6
  i=4, 6 * 4 = 24
'''

# factorial() 호출
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print("---------")

# gobN() 호출
print(gobN(1))
print(gobN(2))
print(gobN(3))
print(gobN(4))