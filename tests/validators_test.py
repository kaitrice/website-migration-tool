"""
Test validator functions
"""
from tool.validators import is_url


def test_is_url():
    """
    Test "is url" function
    """
    assert is_url('') is not False
    assert is_url('domain.com') is not False
    assert is_url('https://domain.com') is True
