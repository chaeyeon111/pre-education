import random

#임의의 수 저장
a = random.randint(1,30)
b = random.randint(1, 30)


#문제를 출력
print(a, "+" , b, "=")

#답을 입력받아 x에 저장합니다. (문자열로 저장합니다.)
x = input()
c = int(x)

if a + b == c:
    print("천재")


else:
    print("바보")
