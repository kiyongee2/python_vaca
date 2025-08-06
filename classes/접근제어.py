# 정보 은닉 - 멤버 변수에 접근 제어
'''
class BankAccount:
    def __init__(self):
        self.__ano = ""    #계좌 번호
        self.owner = ""  #예금주
        self.balance = 0 #잔고

# 기본 생성자 호출
account = BankAccount()
# account.ano = "11-22-3333" #접근 가능(public 속성)
# 멤버변수에 밑줄을 2개 넣으면 접근 제한됨(private 속성)
print(account.__ano) # AttributeError: 
'''

class BankAccount:
    def __init__(self):
        self.__ano = ""
        self.__owner = ""
        self.__balance = 0

    # 계좌 번호 입력 메서드(set + 멤버변수())
    def set_ano(self, ano):
        self.__ano = ano

    # 계좌 번호 반환 메서드
    def get_ano(self):
        return self.__ano
    
    # 예금주 입력 메서드
    def set_owner(self, owner):
        self.__owner = owner

    # 예금주 반환 메서드
    def get_owner(self):
        return self.__owner
    
    # 잔고 입력 메서드
    def set_balance(self, balance):
        self.__balance = balance

    # 잔고 반환 메서드
    def get_balance(self):
        return self.__balance
    
# 기본 생성자 호출
account = BankAccount()

# 계좌 정보 입력
account.set_ano("11-22-3333")
account.set_owner("나저축")
account.set_balance(10000)

# 계좌 정보 출력
print("게좌번호:", account.get_ano())
print("예금주:", account.get_owner())
print("잔고:", account.get_balance())
