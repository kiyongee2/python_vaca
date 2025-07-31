# 학생의 성적 통계
student_list = [
    {"name": "이대한", "kor": 80, "eng": 80, "math": 75},
    {"name": "박민국", "kor": 70, "eng": 65, "math": 60},
    {"name": "오상식", "kor": 75, "eng": 70, "math": 50},
    {"name": "최지능", "kor": 90, "eng": 95, "math": 90},
]

# 첫번째 요소 검색
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["kor"])

print("===== 성적표 =====")
print(" 이름 국어 영어 수학")
for st in student_list:
    print(f'{st["name"]} {st["kor"]}  {st["eng"]}   {st["math"]}')

print("== 개인별 총점과 평균 ==")
print(" 이름  총점  평균")
for st in student_list:
    total = st["kor"] + st["eng"] + st["math"]
    average = total / 3
    print(f'{st['name']} {total}  {average:.2f}')

# 과목별 총점과 평균
sum_subj = [0, 0, 0]  
avg_subj = [0.0, 0.0, 0.0]

# 총점 계산
for st in student_list:
    sum_subj[0] += st["kor"]
    sum_subj[1] += st["eng"]
    sum_subj[2] += st["math"]

# 평균 계산
n = len(student_list)
avg_subj[0] = sum_subj[0] / n
avg_subj[1] = sum_subj[1] / n
avg_subj[2] = sum_subj[2] / n

print("== 과목별 총점과 평균 ==")
print(f'국어 총점: {sum_subj[0]}')
print(f'영어 총점: {sum_subj[1]}')
print(f'수학 총점: {sum_subj[2]}')
print(f'국어 평균: {avg_subj[0]}')
print(f'영어 평균: {avg_subj[1]}')
print(f'수학 평균: {avg_subj[2]}')