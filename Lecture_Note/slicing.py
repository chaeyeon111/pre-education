text = "hello world"
text = text[ 1:5 ]

print(text)

list = [ 0, 1, 2, 3, 4, 5 ]
list = list[ 1:3 ]

print(list)

#slicing에서 값 이외에 string값도 가능하다.
def substring(text, start, end):
    return text[start:end]


my_text = "Hello world"
between_2_5 = substring(my_text, 2, 5)
print(between_2_5)
