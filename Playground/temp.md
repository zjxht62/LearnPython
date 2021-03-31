# 循环中的else

## 什么时候被调用？
循环正常结束的时候被调用
+ for循环循环到末尾
+ while循环条件为False

如果被break掉，那么else就不会执行

举例：判断10以内的素数（for循环版本）
```python
for i in range(2, 10):
    #如果当前的数被2到本身-1都无法整除，那么循环正常结束，执行else  
    for j in range(2, i):
        if (i % j) == 0:
            print(i, 'equals', j, '*', i//j)
            #触发break，不会执行else
            break
    else:
        print(i, 'is prime number')
```
举例：判断10以内的素数（while循环版本）
```python
for i in range(2, 10):
    j = 2
    #当循环条件为false时跳出循环，执行else
    while j < i:
        if (i % j) == 0:
            print(i, 'equals', j, '*', i // j)
            break
        else:
            j += 1
    else:
        print(i, 'is prime number')
```

