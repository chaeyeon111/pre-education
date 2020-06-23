#time 모듈을 임포트합니다.
import time

#input
input("엔터를 누르고 20초를 셉니다.")

#start time을 기록합니다.
start = time.time()

#end time을 기록합니다.
input("20초 뒤에 다시 엔터를 누릅니다.")

end = time.time()


# 차이 variable을 "et"에 기록합니다.
et = end - start


#실제 차이를 기록합니다.
print("실제 시간 : ", et, "초")

#음의 부호를 빼기 위해 abs를 이용하였습니다.
print("차이 : ", abs(et - 20), "초")
