import pytest
@pytest.fixture(scope='function', params=[{'text':'哈哈'}])
def func_scope(request):
    text = request.param['text']
    return '通过固件取出的text:' + text


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


@pytest.fixture(scope='class')
def class_scope():
    pass


def test_multi_scope(sess_scope, mod_scope, func_scope):
    print("我是func_scope返回的", func_scope)
    pass


@pytest.mark.usefixtures('class_scope')
class TestClassScope:
    def test_1(self):
        pass

    def test_2(self):
        pass