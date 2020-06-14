'''
1.
문자열의 역순이 문자열과 동일하면 팰린드롬이라고 한다.
예를 들어, "토마토"는 팰린드롬이지만, "radio"는 팰린드롬이 아니다.
문자열이 주어지면 python 함수를 작성하여 팰린드롬인지 여부를 확인하시오.

테스트코드
<입력>
print(is_palindrome("radio"))
print(is_palindrome("토마토"))

<출력>
False
True
'''


def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False


def length(s):
    for cut in range(len(s), 0, -1):
        for start in range(0, len(s)):
            cutStr = s[start:start + cut]
            # 자른 string 전달
            if is_palindrome(cutStr) == True:
                return len(cutStr)

            if start + cut >= len(s):
                break


print(is_palindrome("radio"))
print(is_palindrome("토마토"))
