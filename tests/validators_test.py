from tool.validators import is_url


def test_is_url():
    assert is_url("") == False
    assert is_url("domain.com") == False
    assert is_url("https://domain.com") == True