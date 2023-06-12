user_input = int(input())
j = 1
for i in range(user_input):
    print("{0:^11}".format("*"*j))
    j = j + 2
