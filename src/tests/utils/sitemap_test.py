"""
Test sitemap functions
"""

from src.tool.utils.sitemap import find_sitemap


def test_find_sitemap():
    """
    Test "find sitemap" function
    """
    assert find_sitemap('') == ''
    assert find_sitemap('https://github.com/') == 'https://github.com/sitemap.php'
