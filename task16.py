user_dict = {"name": None, "age": None}
user_input1, user_input2 = input().split(" ")
user_dict["name"] = user_input1
user_dict["age"] = user_input2
if user_dict["age"] >= "20":
    age_20 = "성인"
print(user_dict, ", "+age_20)
