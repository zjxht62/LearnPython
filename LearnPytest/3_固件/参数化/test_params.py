import pytest


# 定义一个固件
# request是一个默认固件
@pytest.fixture(params=[('redis', '6379'), ('elastincsearch', '9200')])
def param(request):
    return request.param


# 定义一个自动执行的固件
@pytest.fixture(autouse=True)
def db(param):
    print('\nSucceed to connect %s:%s' % param)

    yield

    print('\nSucceed to close %s:%s' % param)


def test_api():
    assert 1 == 1
