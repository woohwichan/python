"""
40. interleave()를 두 개의 리스트를 인자로 받아서, 
두 리스트를 번갈아가면서 이어붙인 새로운 리스트를 반환하도록 수정하시오. 
인자로 들어오는 두 리스트의 길이는 같다고 가정하시오.
(단, 선언된 리스트, 출력문은 수정하지 않고 구성하시오.)
"""


def interleave(list1, list2):
    new_list = []
    for i in range(len(num_list1)):
        new_list.append(num_list1[i])
        new_list.append(num_list2[i])
    return new_list


###수정 금지###
num_list1 = ['a', 'b', 'c', 'd', 'e']
num_list2 = [1, 2, 3, 4, 5]

print("result : ", interleave(num_list1, num_list2))
###수정 금지###