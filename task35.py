"""
35. add_list()을 두 개의 리스트를 인자로 받아서 같은 위치의 리스트 값을 더한 리스트를 반환하도록 수정하시오. 
만약 두 개의 리스트 중 인자가 숫자가 아닌 값이 있거나 크기가 다를 경우 Error를 반환하도록 작성하시오. 
(단, 선언된 list값, 출력문은 수정하지 않고 구성하시오.)
"""


def add_list(list1, list2):
    new_list = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            k = list1[i] + list2[i]
            new_list.append(k)
        return new_list
    else:
        return "Error"
    
    pass


###수정 금지###
num_list = [1, 2, 3, 4, 5, 6]
count_num_list = [5, 5, 5, 5, 5, 5]
fail_num_list = [5, 5]
fail_str_list = [5, "str"]

print("success case : ", add_list(num_list, count_num_list))
print("fail size error case : ", add_list(num_list, fail_num_list))
print("fail str error case : ", add_list(num_list, fail_str_list))
###############