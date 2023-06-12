user_input = input()
list1 = list(user_input)
for i in range(list1.count(" ")):
    list1.remove(" ")
print(list1)
