# 은행 시스템

def main():
    balance = 0 # 잔고(전역 변수 - 값이 유지)

    while True:
        print("=======================================")
        print("1.입금 | 2.출금 | 3.잔액 조회 | 4.종료")
        print("=======================================")

        # try ~ except 구문은 오류(예외)를 처리한다.
        try:
            choice = input("선택> ")  #메뉴 입력
            # print(type(choice)) # str
            
            if choice == '1':
                # print("입금")
                amount = int(input("입금액> ")) #입금액
                balance += amount #잔고 = 잔고 + 입금액
                print(f"입금되었습니다. 현재 잔액: {balance}원")
            elif choice == '2':
                # print("출금")
                amount = int(input("출금액> ")) #입금액
                if amount > balance:
                    print("잔액이 부족합니다.")
                else:
                    balance -= amount #잔고 = 잔고 - 출금액
                    print(f"출금되었습니다. 현재 잔액: {balance}원")
            elif choice == '3':
                # print("잔액 조회")
                print(f"현재 잔액> {balance}원")
            elif choice == '4':
                print("종료!")
                break
            else:
                print("메뉴를 잘못 선택했어요. 다시 입력하세요")
        except ValueError:
            print("숫자를 입력하세요.")

# 실행 - main() 호출
main()