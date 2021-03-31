from . import m1
from .m1 import add
# for i in range(2, 100):
#     if i == 2:
#         print(i)
#         continue
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)


# for i in range(2, 10):
#     for j in range(2, i):
#         if (i % j) == 0:
#             print(i, 'equals', j, '*', i//j)
#             break
#     else:
#         print(i, 'is prime number')


# for i in range(2, 10):
#     j = 2
#     while j < i:
#         if (i % j) == 0:
#             print(i, 'equals', j, '*', i // j)
#             break
#         else:
#             j += 1
#     else:
#         print(i, 'is prime number')

list = [1, 2, 3, 4, 5]
for x in list:
    continue
    print(x)
else:
    print("else")
