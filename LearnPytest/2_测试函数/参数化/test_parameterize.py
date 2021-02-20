import pytest
@pytest.mark.parametrize('passwd', ['123456', 'asdfvsdv', '123sfa23fdsfs'])
def test_passwd_length(passwd):
    assert len(passwd) >= 0
