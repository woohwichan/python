dictionary_example = {'a': 3, 'b': 5, 'c': 2, 'd': 5, 'e': 6, 'f': 6, 'g': 0}
new_dict = {}
for key, value in dictionary_example.items():
    if not list(dictionary_example.values()).count(value) > 1:
        new_dict[key] = value
print(new_dict)
