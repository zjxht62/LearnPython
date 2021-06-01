# from . import m1
# from .m1 import add
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

# list = [1, 2, 3, 4, 5]
# for x in list:
#     continue
#     print(x)
# else:
#     print("else")
#
#
# files = 'a',
# files1 = ('a',)
# print(type(files))
# print(type(files1))

# import sys
# if __name__ == '__main__':
#     env = sys.argv[1]
#     parent_task_list = sys.argv[2:]
#     non_repeating_parent_task_list = list(set(parent_task_list))
#     non_repeating_parent_task_list.sort(key=parent_task_list.index)
#
#     print(env)`
#     print(non_repeating_parent_task_list)
girls = ['alice', 'bernice', 'clarice', 'cat']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    # 建立字典，key为首字母，value默认为[]，之后添加girl全名
    letterGirls.setdefault(girl[0], []).append(girl)
    print("输出每次的letterGirls", letterGirls)
print([b + "+" + g for b in boys for g in letterGirls[b[0]]])