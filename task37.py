"""
37. sum_dic_values()를 하나의 딕셔너리 인자를 받아 key와 value를 각각 리스트로 변환하여 2가지 리스트를 반환하도록 수정하시오. 
(단, 선언된 딕셔너리, 출력문은 수정하지 않고 구성하시오.)
"""


def sum_dic_values(dictionary) :
    key_list = []
    value_list = []
    for key in dictionary.keys():
        key_list.append(key)
    for value in dictionary.values():
        value_list.append(value)
    return key_list, value_list


###수정 금지###
test_dictionary = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
check_key, check_value = sum_dic_values(test_dictionary)

print("key : ", check_key)
print("values : ", check_value)
###수정 금지###