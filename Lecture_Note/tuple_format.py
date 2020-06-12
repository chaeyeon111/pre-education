ages = {'Tod' : 35, 'Jane' : 23, 'Paul' : 62}

#두 경우 다 같은 말

for a in ages.items():
    print('{}의 나이는:{}'.format(a[0], a[1]))

for a in ages.items():
    print('{}의 나이는:{}'.format(*a))    # 두 출력 결과가 같습니다.
