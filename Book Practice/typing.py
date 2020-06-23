import random
import time

w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]

#문제 번호
n = 1

print("[타자게임] 준비 되면 엔터!")

#사용자가 enter를 누를 때까지 기다립니다.
input()


#시작 시간을 기록합니다.

start = time.time()

#단어 리스트에서 아무것이나 하나 뽑습니다.
q = random.choice(w)

#문제를 다섯 번 반복합니다.

while n<= 5:
    print("*문제", n)
    print(q)

    x = input()

    if q == x:
        print("통과!")

        n = n + 1
        q = random.choice(w)

    else:
        print("오타! 다시 도전!")


end = time.time()
et = start - start

et = format(et, ".2f")
print("타자 시간:", et, "초")
