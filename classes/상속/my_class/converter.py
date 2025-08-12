# 단위 변환기 클래스
'''
    1MB = 1024KB -> 변환상수 - 1024
    1inch = 25mm -> 변환상수 - 25
'''
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from   #단위
        self.units_to = units_to       #변환할 단위
        self.factor = factor           #변환 상수

    def convert(self, value):
        return value * self.factor
    
if __name__ == "__main__":
    # 생성자 호출
    con1 = ScaleConverter("MB", "KB", 1024)
    print("2MB를 KB로 변환하기")
    print(f"{con1.convert(2)}{con1.units_to}") #2048KB

    con2 = ScaleConverter("inches", "mm", 25)
    print("5인치를 mm로 변환하기")
    print(f"{con2.convert(5)}{con2.units_to}") #125mm