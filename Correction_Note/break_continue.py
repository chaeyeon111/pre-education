"""
다음 코드는 numbers에 있는 튜플을 받아들여서 튜플의 첫번째 숫자를 두번째 숫자로 나누는 일을 합니다.
이 때, b가 0이면 0으로 나눌 수는 없습니다.라고 출력하는데요.
이 if else문에서 continue문을 이용하여 else를 사용하지 않도록 변경해 보세요.
"""

# 리스트 안에 두 개의 튜플이 존재한다.

numbers = [ (1,2),(10,0) ]

#for in 반복문이 쓰였고,
for a,b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue
    print("{}를 {}로 나누면 {}".format(a,b,a/b))
