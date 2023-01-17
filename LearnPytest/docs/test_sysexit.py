import pytest
# 测试是否抛出了指定的异常
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()