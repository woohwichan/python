def find_common_chars(str1, str2):      # find_common_chars 함수 정의
    common_chars = []       # 공통된 문자를 담을 리스트
    for char in str1:       # str1의 문자들을 하나씩 char에 대입
        if char in str2 and char not in common_chars:    # char이 str2에 있고, common_chars에 없으면
            common_chars.append(char)       # common_chars에 char 추가
    return ''.join(common_chars)        # common_chars를 문자열로 반환


user_input1, user_input2 = input().split(", ")
list1 = list(user_input1)
for i in range(list1.count(" ")):
    list1.remove(" ")
list2 = list(user_input2)
for i in range(list2.count(" ")):
    list2.remove(" ")
common = find_common_chars(list1, list2)        # find_common_chars 함수를 호출하여 반환된 값을 common에 대입
print(common)       # common 출력
