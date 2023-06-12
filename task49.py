user_input = input().split(", ")
list1 = [[]]
for i in user_input:
    for j in range(len(list1)):
        list1.append(list1[j] + [i])
list1.sort(key=len)
for i in range(len(list1)):
    print(list1[i])
