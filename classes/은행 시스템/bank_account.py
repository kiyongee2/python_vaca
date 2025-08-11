# 은행 계좌 클래스 정의

class BankAccount:
    def __init__(self):
        self.balance = 0#잔고
        self.transaction_history = [] #거래내역 리스트
  
    # 입금 기능
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(('입금', amount)) #요소를 튜플 저장(입금 내역)
        print(f"{amount}원 입금되었습니다. 현재 잔액: {self.balance}원")

    # 출금 기능
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"잔액이 부족합니다. 현재 잔액: {self.balance}원")
        else:
            self.balance -= amount
            self.transaction_history.append(('출금', amount)) #출금 내역
            print(f"{amount}원 출금되었습니다. 현재 잔액: {self.balance}원")

    # 잔액 조회
    def get_balance(self):
        return self.balance
    
    # 거래내역 조회
    def get_transaction_history(self):
        return self.transaction_history #거래내역 리스트 반환
    
# main() 정의
def main():
    # 은행 계좌 인스턴스 생성
    account = BankAccount()

    while True:
        print("======================================================")
        print("1.입금 | 2.출금 | 3.잔액 조회 | 4.거래 내역 | 5.종료")
        print("======================================================")

        try:
            choice = input("선택> ")  #메뉴 입력
            
            if choice == '1':
                amount = int(input("입금액> ")) #입금액
                account.deposit(amount) #deposit() 호출
            elif choice == '2':
                amount = int(input("출금액> ")) #입금액
                account.withdraw(amount) #withdraw() 호출
            elif choice == '3':
                print(f"현재 잔액> {account.get_balance()}원")
            elif choice == '4':
                print("\n[거래 내역]")
                print(account.transaction_history) #리스트 출력
                '''
                for type, amount in account.transaction_history:
                    print(f"- {type}: {amount}원")
                '''
                for transaction in account.transaction_history:
                    print(f"- {transaction[0]}: {transaction[1]}원")
            elif choice == '5':
                print("종료!")
                break
            else:
                print("메뉴를 잘못 선택했어요. 다시 입력하세요")
        except ValueError:
            print("숫자를 입력하세요.")

# main() 호출 - 실행
main()
