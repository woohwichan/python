44. 다음 코드의 출력 결과를 쓰시오.

```
def abin() :
    return
def aben() :
    return None
def abf() :
    return False
def abz() :
    return 0
def abt() :
    return True
def abnv() :
    return abt

print("Same") if abin() == aben() else print("Different")
print("Same") if abf() == abz() else print("Different")
print("Same") if abz() == abt() else print("Different")
print("Same") if abt() == abnv() else print("Different")
```

답 : 
Same
Same
Different
Different
