"""
36. task20.py의 is_palindrome()을 하나의 문자 인자를 받아 팰린드롬의 여부를 반환하도록 수정하시오.
(팰린드롬 : 앞에서 읽으나 뒤에서 읽으나 같은 단어 또는 문장)
"""


def is_palindrome(string):
    string_list = list(string)
    string_reverse = list(reversed(string_list))
    if string_list == string_reverse:
        return success_palindrome
    else: 
        return fail_palindrome
    pass


###수정 금지###
success_palindrome = "rise to vote sir"
fail_palindrome = "python midterm"

if is_palindrome(success_palindrome) :
    print("case1 : Success")
else : 
    print("Error")

if is_palindrome(fail_palindrome) :
    print("case2 : Fail")
else : 
    print("Error")
###수정 금지###