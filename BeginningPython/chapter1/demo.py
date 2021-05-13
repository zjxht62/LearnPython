# Python中的整除和求余（求模）
# 在Python中，总是将商向下圆整，比如：-3.3333就会圆整到-4、3.333圆整到3
print(10 // 3)  # 3
print(-10 // 3)  # -4
print(10 // -3)  # -4
print(-10 // -3)  # 3

# 数学中取余的规则：如果a与d是整数，d非零，那么余数`r`满足`a=q*d+r`,`q`为整数，且`0<=|r|<|d|`
# 所以对于 10 % -3，会存在两个符合条件的情况
# 正余数：d=-3 r=1
# 副余数：d=-4 r=-2
# 在求余（求模）运算中，Python会取向下圆整的商来计算余数，也可以看出规律，余数的符号和除数一样
print(10 % 3)  # 1
print(10 % -3)  # -2
print(-10 % 3)  # 2
print(-10 % -3)  # -1

print((1 + 3j) * (9 + 4j))  # (-3+31j)
