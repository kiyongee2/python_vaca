# 내장 함수(Built-in-Function)
a = [1, 2, 3]
t = (1, 2, 3) #튜플

# 합계
print(sum(a)) #6
print(sum(t)) #6

# 최대값
print(max(a)) #3
print(max(t)) #3

# 절대값
print(abs(-6)) #6

# 반올림 - round(숫자, 자리수)
# -1:일의 자리
print(round(6.394, 1)) #6.4
print(round(6.394, 0)) #6.0
print(round(6.394)) #6
print(round(1506, -1)) #1510

# 1 ~ n 까지 더하기
'''
   ** 계산 복잡도 **
   sum_n(n) - 덧셈 n번 -> O(n) : 빅O 표기
   sum_n2(n) - 덧셈1, 곱셈1, 나눗셈1(총 3번)-> O(3)
'''
def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def sum_n2(n):
    total = (n * (n + 1)) / 2
    return int(total)

result1 = sum_n(10)
print("합계1:", result1)  #55

result2 = sum_n2(10)
print("합계2:", result2)  #55

# 내장함수 - sum()
v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(v)) #55