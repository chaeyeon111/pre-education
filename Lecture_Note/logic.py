def return_false():
    print("함수 return_false")
    return False

def return_true():
    print("함수 return_true")
    return True

print("테스트!")
a = return_false()
b = return_true()

if a and b:
    print(True)

else:
    print(False)


print("테스트2")

if return_true() and return_true():
    print("True")

#만약 if 문이 실행되면 else문은 실행되지 않는다.
else:
    print(False)
