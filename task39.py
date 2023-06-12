"""
39. decimal_to_binary()는 인자로 받은 정수를 4진수로 표현하여 반환하는 함수이다. 
decimal_to_binary()를 인자로 받은 정수를 2진수로 반환하도록 수정하시오.
그후, 사용자로부터 입력받은 숫자를 2진수로 반환하시오.
"""


def decimal_to_binary(num):
    digits = '0123'
    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        remainder = num % 2
        result = digits[remainder] + result
        num //= 2
    return result


user_input = int(input())
print(decimal_to_binary(user_input))
