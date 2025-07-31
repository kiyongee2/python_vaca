# 리스트를 매개변수로 사용
'''
# for ~ range() 구문
def calculate2(arr):
    sum_v = 0 #합계
    n = len(arr)  #개수
    for i in range(0, n):
        sum_v += arr[i]
    return sum_v

# for in 리스트이름
def calculate(arr):
    sum_v = 0 #합계
    for val in arr:
        sum_v += val
    return sum_v

a = [1, 2, 3, 4]
total = calculate(a) #함수 호출
print("합계:", total)
'''

def list_copy(a): #a = [1, 2, 3, 4]
    a2 = [] #빈 리스트
    for val in a:
        a2.append(4 * val) #4의 배수
    return a2

# 리스트에 복사 - 배수로 저장
v = [1, 2, 3, 4]

v2 = list_copy(v)
print(v2) #[4, 8, 12, 16]
