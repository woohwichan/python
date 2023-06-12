"""
3. 사용자로부터 자연수를 입력받아 0부터 자연수까지 출력하시오.
"""
num = int(input())

###정답란###
for i in range(0, num + 1):
    print(i, end=" ")
