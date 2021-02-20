# 测试抛出异常
# 经常需要测试是否如期抛出预期的异常，以确定异常处理模块生效
import pytest
def test_raises():
    with pytest.raises(TypeError) as e:
        connect('localhost', '6379')
    exec_msg = e.value.args[0]
    assert exec_msg == 'port type must be int'