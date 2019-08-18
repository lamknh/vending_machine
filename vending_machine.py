productNumber = {1: "아이시스", 2: "레몬워터", 3: "옥수수 수염차", 4: "초가을 우엉차", 5: "트레비",
                     6: "밀키스", 7: "펩시", 8: "핫식스", 9: "칠성사이다", 10: "코코리치 망고", 11: "립톤",
                     12: "트로피카나 사과맛", 13: "트로피카나 포도맛", 14: "가나", 15: "레쓰비 마일드 커피",
                     16: "칸타타", 17: "레쓰비 카페타임 라떼", 18: "게토레이", 19: "코코 포도", 20: "잔치집 식혜"}

productPrice = {1: 600, 2: 1500, 3: 1300, 4: 1300, 5: 1000, 6: 800, 7: 800, 8: 1000, 9: 1000,
                    10: 1000, 11: 1000, 12: 1000, 13: 1000, 14: 600, 15: 600, 16: 1000, 17: 1000,
                    18: 800, 19: 800, 20: 800}

productStock = {1: 10, 2: 10, 3: 10, 4: 10,
                    5: 7, 6: 7, 7: 7, 8: 7,
                    9: 3, 10: 3, 11: 3, 12: 3,
                    13: 1, 14: 1, 15: 1, 16: 1,
                    17: 0, 18: 0, 19: 0, 20: 0}

def printing_product_name():
    for number in productNumber.keys():
        print("%d번 %s(%d원)" % (number, productNumber[number], productPrice[number]))

def input_money():
    global money
    money = int(input("투입할 금액을 입력해주세요: "))

class SelectingVM(object):
    def __init__(self, selection):
        self.selection = selection

    def selecting(self):
        self.selection = int(input("원하시는 제품의 번호를 입력해주세요 \n (없으시다면 0을 입력해주세요): "))
        if self.selection == 0:
            returning()
        else:
            SelectingVM.comparing_stock(self)

    def comparing_stock(self):
        if productStock[self.selection] == 0 :
            print("# 재고가 부족합니다 #")
            print("** 재고 부족 SMS 알림이 발송됩니다 **")
            SelectingVM.vendingmachine_ending(self)
        else :
            SelectingVM.comparing_money(self)

    def comparing_money(self):
        global money
        if money >= productPrice[self.selection]:
            money -= productPrice[self.selection]
            productStock[self.selection] -= 1
            print("제품 '%s'이(가) 나왔습니다." % (productNumber[self.selection]))
            print("현재 잔액: ", money)
            SelectingVM.vendingmachine_ending(self)
        else:
            print("# 잔액이 부족합니다 #")
            returning()

    def vendingmachine_ending(self):
        answer = str(input("자판기 실행을 계속할까요? (y/n)"))
        if answer == "y":
            printing_product_name()
            SelectingVM.selecting(self)
        elif answer == "n":
            returning()
        else:
            print("잘못 입력하셨습니다. y/n 둘 중 하나만 입력 바랍니다.")
            SelectingVM.vendingmachine_ending(self)


def returning():
        print("거스름돈을 반환합니다")
        global money
        thousand = money//1000
        fivehundred = (money - (thousand * 1000)) // 500
        onehundred = (money - (thousand * 1000 + fivehundred * 500)) // 100

        amount_thousand = 5
        amount_fivehundred = 5
        amount_onehundred = 5

        amount_thousand -= thousand
        amount_fivehundred -= fivehundred
        amount_onehundred -= onehundred

        if amount_thousand > 0 and amount_fivehundred > 0 and amount_onehundred > 0:
            print("")
            print ("1000원짜리: %d, 500원짜리: %d, 100원짜리: %d" % (thousand, fivehundred, onehundred))
            print("")
            print("# # # 자판기 프로그램을 종료합니다 # # #")
        else :
            print("")
            print(" 반환금이 부족합니다 ")
            print(" 주인에게 문의해주세요 010 - xxxx - xxxx ")
            print("** 반환금 부족 SMS 알림이 발송됩니다 **")
            print("# # # 자판기 프로그램을 종료합니다 # # #")



def main():

    print ("# # # 자판기 프로그램을 가동합니다 # # #")
    print ("")
    printing_product_name()
    print("")
    input_money()
    SelectingVM(object).selecting()

if __name__ == "__main__":
    main()