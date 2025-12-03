"""
Test format functions
"""
from src.tool.utils.format import format_url


def test_format_url():
    """
    Test "format url" function
    """
    assert format_url('') == ''
    assert format_url('https://github.com') == 'https://github.com/'
    assert format_url('https://github.com/') == 'https://github.com/'
    assert format_url('https://github.com/kaitrice') == 'https://github.com/'
