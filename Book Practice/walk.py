import turtle as t
import random

t.shape("turtle")
t.speed(0)


for x in range(500):
    a = random.randint(1,360)
    #거복이 방향ㅇ을 a 각도로 돌립니다.
    t.setheading(a)

    #1~20 사이에 있는 아무 수나 골라 b에 저장합니다.

    b = random.randint(1,20)


    # 10을 b로 고칩니다.
    t.forward(b)

