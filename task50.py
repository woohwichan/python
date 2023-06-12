def error(error_check):
    for i in error_check:
        if i.isdigit():
            i = int(i)
            if 10 >= i >= 2:
                pass
            else:
                return True
        elif i == "A" or i == "K" or i == "Q" or i == "J":
            pass
        elif len(set(error_check)) >= 5:
            return True
        else:
            return True
    return False


def four_card(four_card_check):
    for four_i in four_card_check:
        if four_card_check.count(four_i) == 4:
            return True
        else:
            return False


def three_card(three_card_check):
    for three_i in three_card_check:
        if three_card_check.count(three_i) == 3:
            return True
        else:
            return False


def full_house(full_house_check):
    if three_card(full_house_check) and len(set(full_house_check)) == 2:
        return True
    else:
        return False


def two_pair(two_pair_check):
    if len(set(two_pair_check)) == 3:
        return True
    else:
        return False


def one_pair(one_pair_check):
    if len(set(one_pair_check)) == 4:
        return True
    else:
        return False


def no_pair(no_pair_check):
    if len(set(no_pair_check)) == 5:
        return True
    else:
        return False


user_input = input().split(", ")
if error(user_input):
    print("Error")
elif four_card(user_input):
    print("Four Card")
elif full_house(user_input):
    print("Full House")
elif three_card(user_input):
    print("Three Card")
elif two_pair(user_input):
    print("Two Pair")
elif one_pair(user_input):
    print("One Pair")
elif no_pair(user_input):
    print("No Pair")
else:
    print("Error")
