# 온도 변환기
'''
   단위 변환기를 상속(확장)함
   class 클래스이름(상위클래스):
   converter 모듈의 ScaleConverter 사용
   예) 화씨온도(F) = 섭씨온도(C) * 1.8 + 32
'''
from my_class.converter import ScaleConverter

class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)
        self.offset = offset  #변환 상수

    def convert(self, value): #부모 클래스의 convert() 재정의
        return super().convert(value) + self.offset

'''
# Converter 생성자 호출
conv = Converter('C', 'F', 1.8, 32)
print("섭씨온도 23도를 화씨온도로 변환")
print(f"{conv.convert(23)}{conv.units_to}") #73.4F
'''

# 단위변환기를 사용해서 2kg을 2000g으로 변환하세요.
print("2kg을 2000g으로 변환하기")
con = ScaleConverter("kg", "g", 1000)
print(f"{con.convert(2)}{con.units_to}") #2000g


