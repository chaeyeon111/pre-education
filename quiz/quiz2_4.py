'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.movie(5000,'마트')
multi_card.movie(10000,'영화관')
multi_card.movie(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''


class Multi_card:
    def __init__(self):
        self.money = 0
        print("카드가 발급되었습니다")

    def charge(self, num):
        self.money += num
        print(str(num) + "가 충전되었습니다.")

    def movie(self, num, x):

        if x == '영화관':
            if self.money - num * 0.8 < 0:
                print("잔액이 부족합니다.")

            else:
                self.money -= num * 0.8
                print("{}에서 {:.0f}원 사용했습니다.".format(x, num * 0.8))

        elif x == '마트':
            if self.money - num * 0.9 < 0:
                print("잔액이 부족합니다.")

            else:
                self.money -= num * 0.9
                print("{}에서 {:.0f}원 사용했습니다.".format(x, num * 0.9))

        elif x == '교통':
            if self.money - num * 0.9 < 0:
                print("잔액이 부족합니다.")

            else:
                self.money -= num * 0.9
                print("{}에서 {:.0f}원 사용했습니다.".format(x, num * 0.9))




        else:
            if self.money - num < 0:
                print("잔액이 부족합니다.")

            else:
                self.money -= num
                print("{}에게 {:.0f}원 사용했습니다.".format(x, num))

    def print(self):
        print('잔액이 {:.0f}입니다.'.format(self.money))


multi_card = Multi_card()
multi_card.charge(20000)
multi_card.movie(5000, '마트')
multi_card.movie(10000, '영화관')
multi_card.movie(2000, '교통')
multi_card.print()
