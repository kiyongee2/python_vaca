# for 반복문
# range(시작값, 종료값, 증감값) 함수

print(list(range(1, 10, 1))) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 2))) #[1, 3, 5, 7, 9]


# 1 ~ 10 자연수 출력
for i in range(1, 11, 1):
    print(i)
print("*******")

# 1 ~ 10중 짝수 출력 및 합계 계산
hap = 0  #합계를 저장할 변수 초기화
count = 0 #개수 초기화
for i in range(1, 11, 1):
    if i % 2 == 0:
        count += 1 #count = count + 1
        hap += i #hap = hap + i
        print(i, end=' ') #2 4 6 8 10

print("\n합계:", hap)
print("개수:", count)
print("평균: ", hap / count) #평균 = 합계 / 개수

