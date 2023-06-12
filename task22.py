new_dict = {}
fruits = ["apple", "banana", "orange", "apple", "grape", "banana", "apple", "melon", "grape", "orange"]
for i in fruits:
    a = fruits.count(i)
    new_dict[i] = a
print(new_dict)
