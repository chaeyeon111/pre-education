"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는 
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오.

예시
<입력>
EAST
<출력>
east

<입력>
hello
<출력>
HELLO

<입력>
안녕
<출력>
입력 형식이 잘못되었습니다.

"""

string = str(input("Write : "))
newstring = ''
count1 = 0
count2 = 0
count3 = 0

for a in string:
    if (a.isupper()) == True:
        count1 += 1
        newstring +=(a.lower())

    elif (a.islower()) == True:
        count2 += 1
        newstring += (a.upper())


    elif (a.isspace()) == True:
        count3 += 1
        newstring += a

    else:
        print("입력 형식이 잘못되었습니다.")
        break


print("Uppercase -", count1)
print("Lowercase -", count2)
print("Spaces -", count3)
print("Error -", len(string)- count1 -count2 - count3)

print("After changing cases:")
print(newstring)

