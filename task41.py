"""
41. task25.py의 most_frequent()를 한 개의 문자열을 인자로 받아서 가장 많이 등장하는 문자와 
그 등장횟수를 튜플 형태로 반환하도록 수정하시오.
등장하는 횟수가 같은 문자와 대문자가 없다고 가정하고 구성하시오.
(단, 선언된 문자열, 출력문은 수정하지 않고 구성하시오.)
"""
from collections import Counter


def most_frequent(string):
    string_list = list(string)
    a = Counter(string_list)
    count = a.most_common(1)
    return count
    pass


###수정 금지###
test_str = "python programming midterm"
print(most_frequent(test_str))