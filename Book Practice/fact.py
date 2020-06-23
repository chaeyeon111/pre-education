def factorial(n):
    #곱을 구하기 위한 변수 fact 시작 값을 1로 지정
    fact = 1

    #range(1, n+1)로 1,2,..., n까지 반복
    for x in range(1, n+1):
        fact = fact * x


    return fact

print(factorial(5))
print(factorial(10))
