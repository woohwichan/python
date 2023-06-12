user_input = int(input())
if user_input > 1:
    for j in range(2, user_input):
        if (user_input % j) == 0:
            print("합성수")
            break
    else:
        print("소수")
