# try:
#     print('我是正常执行')
#     raise Exception("我是异常")
#     print('我是异常之后的代码') # 不会执行
# except Exception as e:
#     print('异常信息', e)


class MyException(Exception):
    pass


# my_exception = MyException()
# raise my_exception


# try:
#     1/0
# except ZeroDivisionError as zde:
#     raise ValueError from zde

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except:
    print('Something wrong happened ...')