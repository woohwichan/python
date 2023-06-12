"""
15. 사용자로부터 입력받은 문자가 변수 hanbat에 포함될 경우 True, 포함되지 않을 경우 False를 출력하시오. 
단 입력받은 문자가 숫자일 경우 “Error”를 출력하시오.
"""

hanbat = "Hanbat National University"

###정답란###
user_input = input()
if user_input.isalpha():
    print(user_input in hanbat)
elif user_input.isdigit():
    print("Error")
else:
    print("Error")
