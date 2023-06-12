user_input1, user_input2 = input().split(" ")
user_input1 = int(user_input1)
user_input2 = int(user_input2)
for i in range(min(user_input1, user_input2), 0, -1):
    if user_input1 % i == 0 and user_input2 % i == 0:
        print(i)
        break
