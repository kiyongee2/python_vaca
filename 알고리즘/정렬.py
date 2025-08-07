# 정렬 - 오름차순, 내림차순
# sort()
numbers = [41, 8, 36, 77, 15]
'''
#오름차순 정렬
numbers.sort() 
print(numbers) #[8, 15, 36, 41, 77]

# 내림차순
numbers.sort(reverse=True)
print(numbers)
'''

# 자리 바꿈(교환)
'''
print(numbers) #[41, 8, 36, 77, 15]
numbers[0], numbers[1] = numbers[1], numbers[0]
print(numbers) #[8, 41, 36, 77, 15]
'''

'''
 버블 정렬
 - 인접한 두 개의 요소를 비교하여 자리를 바꾸는 정렬 알고리즘이다.
 - 오름차순, 내림차순 정렬
 - 매우 느린 알고리즘, 계산복잡도 O(n²)
'''

"""
a = [41, 8, 36, 77, 15]

for i in range(0, 5):
    for j in range(0, 4):
        # 인접 요소 비교 - 자리바꿈
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

   i=0, j=0, 41>8, [8 41 36 77 15]
        j=1, 41>36, [8 36 41 77 15]
        j=2, 41>77, 교환없음
        j=3, 77>15, [8 36 41 15 77]
   i=1, j=0, 8>36 
        j=1, 36>41, 
        j=2, 41>15, [8 36 15 41 77]
        j=3, 41>77
   i=2, j=0, 8>36 
        j=1, 36>15, [8 15 36 41 77] - 오름차순 정렬
   i=3, 교환없음
   i=4,
   i=5, 반복 종료

   print(a) #[8, 15, 36, 41, 77]
"""

# 버블 정렬 - 함수로 구현
def sort_bubble(a):
    n = len(a)  #리스트 요소의 개수
    for i in range(0, n):
        for j in range(0, n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a #a 리스트 반환

arr = [41, 8, 36, 77, 15, 64]
arr2 = sort_bubble(arr)
print(arr2)  #[8, 15, 36, 41, 64, 77]

