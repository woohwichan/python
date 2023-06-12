42. 아래 코드의 결과를 작성하시오.

```
try:
    for a in range(0,4):
        a = a + a
        if a / 2 == 0:
            print(a)
        elif a % 2 == 0:
            print(a+"a")
except:
    print("abc")
```

답 : 
0
abc
