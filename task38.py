"""
38. merge_dict()를 하나의 딕셔너리 인자를 받아와 merge_dict()에 선언된 
count_dict와 하나로 합쳐 반환하도록 수정하시오. 
두 딕셔너리가 같은 key를 가지고 있다면 인자로 받아온 value를 활용한다.
(단, 선언된 딕셔너리, 출력문은 수정하지 않고 구성하시오.)
"""


def merge_dict(dict) :
    count_dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}#수정 금지
    new_dict = count_dict
    for i, j in dict.items():
            new_dict[i] = j
    return new_dict


###수정 금지###
check_dict = {'a' : 3, 'e' : 4, 'f' : 3, 'g' : 5}
sorted_dict = {}
for key, value in sorted(merge_dict(check_dict).items()):
    sorted_dict[key] = value

print("merge result : ", sorted_dict)
###수정 금지###
