# if 문은 조건이 맞으면 한 번 실행하지만 while 반복문은 조건이 맞다면 계속 반복

selected = None
# 세번 물어볼 것

"""
가위,바위, 보 중에 선택하세요 가위
가위,바위, 보 중에 선택하세요 가위
가위,바위, 보 중에 선택하세요 가위
"""

while selected not in ['가위', '바위', '보']:
    selected = input('가위,바위, 보 중에 선택하세요')

"""
선택된 값은 가위
"""

print('선택된 값은', selected)

# for 반복문으로 작성한 코드는 while 반복문으로도 작성할 수 있다.

"""
가위
보
보
"""

patterns = ['가위', '보', '보']

for i in range(len(patterns)):
    print(patterns[i])


#상황에 맞는 반복문을 사용할 것
