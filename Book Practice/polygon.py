import turtle as t

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)


def polygon2(n,a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)



#삼각형을 그립니다.
polygon(3)

#오각형을 그립니다.
polygon(5)

t.up()
t.forward(100)
t.down()

polygon2(3,75)
polygon2(5,100)
