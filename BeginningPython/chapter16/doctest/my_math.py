def square(x):
    """
    计算平方并返回结果
    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x * x


if __name__ == '__main__':
    import my_math
    from doctest import testmod

    testmod(my_math)

#执行python my_math.py -v 会根据文档里的内容来执行测试
#Trying:
#    square(2)
#Expecting:
#    4
#ok
#Trying:
#    square(3)
#Expecting:
#    9
#ok
#1 items had no tests:
#    my_math
#1 items passed all tests:
#   2 tests in my_math.square
#2 tests in 2 items.
#2 passed and 0 failed.
#Test passed.
