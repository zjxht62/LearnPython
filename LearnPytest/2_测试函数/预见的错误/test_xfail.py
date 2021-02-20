import gen as gen
import pytest

@pytest.mark.xfail(gen.__version__ < '0.2.0', reason='not supported until v0.2.0')
def test_api():
    id_1 = gen.unique_id()
    id_2 = gen.unique_id()
    assert id_1 != id_2
