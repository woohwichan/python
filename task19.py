mixed_list = [1, "apple", 3.5, "banana", "orange", 6]
new_list = []
for i in mixed_list:
    if str(i).isalpha():
        new_list.append(i)
    else:
        pass
print(new_list)
