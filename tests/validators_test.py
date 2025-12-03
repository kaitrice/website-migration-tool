"""
Test validator functions
"""
from tool.validators import is_url, is_valid_url


def test_is_url():
    """
    Test "is url" function
    """
    assert is_url('') is False
    assert is_url('domain.com') is False
    assert is_url('https://domain.com') is True

def test_is_valid_url():
    """
    Test "is valid url" function
    """
    assert is_valid_url('') is False
    assert is_valid_url('google.com') is False
    assert is_valid_url('https://google.com') is True
