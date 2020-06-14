'''
2.
년, 월, 일을 입력하면 그 날이 무슨 요일인지 출력하는 함수를 만드세요.
테스트코드
<입력>
print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))
<출력>
연도를 입력하시오 : 2020
월을 입력하시오 : 3
일을 입력하시오 : 13
2020년 3월 13일은 금요일 입니다.
'''

year = int(input("연도를 입력하시오 : "))

month = int(input("월을 입력하시오 : "))

day = int( input("일을 입력하시오 : "))

month_days = [0,31,28,31,30,31,30,31,30,31,30,31,30]

total_days = 0


for year_item in range(1, year):
    total_days = total_days + 365

    if year_item % 400 == 0 and month >= 3:
        total_days = total_days + 1

    elif year_item % 100 == 0:
        pass

    elif year_item % 4 == 0 and month>=3:
        total_days = total_days + 1

    else:
        pass

for month_index in range(1, month):
    total_days = total_days + month_days[month_index]

total_days = total_days + day


if total_days % 7 == 0:
    print(str(year) + "년 " + str(month) + "월 " + str(day) + "일 " + "일요일")

elif total_days % 7 == 1:
    print(str(year) + "년 " + str(month) + "월 " + str(day) + "일 " + "월요일")

elif total_days % 7 == 2:
    print(str(year) + "년 " + str(month) + "월 " + str(day) + "일 " + "화요일")

elif total_days % 7 == 3:
    print(str(year) + "년 " + str(month) + "월 " + str(day) + "일 " + "수요일")

elif total_days % 7 == 4:
    print(str(year) + "년 " + str(month) + "월 " + str(day) + "일 " + "목요일")


elif total_days % 7 == 5:
    print(str(year) + "년 " + str(month) + "월 " + str(day) + "일 " + "금요일")


elif total_days % 7 == 6:
    print(str(year) + "년 " + str(month) + "월 " + str(day) + "일 " + "토요일")





