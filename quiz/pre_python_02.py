""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오


예시
<입력>
첫 번째 수를 입력하세요 : 10
두 번째 수를 입력하세요 : 15
어떤 연산을 하실 건가요? : *

<출력>
150
"""

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    numberA = int(input("첫 번째 숫자를 입력하세요 : "))
    numberB = int(input("두 번째 숫자를 입력하세요 : "))

    selection = int(input("어떤 연산을 하실 껀가요? \n 1. + \n "
                          "2. - \n 3. × \n 4. ÷ \n  어떤 연산을 하실 껀가요? \n "))


    if(selection == 1):
        result = sum(numberA,numberB)
        print("결과는 %d 입니다." %result)

