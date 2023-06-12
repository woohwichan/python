list_example = [4, 15, 30, 22, 11, 3, 6, 12, 22]
new_list = []
for i in list_example:
    for j in range(1, i+1):
        if i % j == 0:
            new_list.append(j)
        else:
            pass
new_list = list(set(new_list))
print(new_list)
