def isprime(a):
    for j in range(2, a+1):
        is_prime = True
        for k in range(2, j):
            if j % k == 0:
                is_prime = False
                break
        if is_prime:
            list1.append(j)
        else:
            continue


prime_number = {}
user_input = input().split(" ")
for i in range(len(user_input)):
    list1 = []
    n = user_input[i]
    if n.isdigit() and int(n) >= 1:
        n = int(n)
        isprime(n)
        prime_number[n] = list1
    else:
        break
print(prime_number)
