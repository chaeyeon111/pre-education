#딕셔너리를 선언합니다.

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

#요소 제거
print("요소 제거 이전:", dictionary)

del dictionary["name"]
del dictionary["type"]

print("요소 제거 이후: ", dictionary)
