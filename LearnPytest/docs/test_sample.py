# pytest会在当前目录及其子目录递归查找test_开头或_test结尾的.py文件来执行
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
