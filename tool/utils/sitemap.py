"""
Utility functions for locating sitemap.
"""

from tool.validators import is_url, is_valid_url


def find_sitemap(base_url: str) -> str:
    """
    Find sitemap from url
    
    :param baseUrl: Valid base url
        :type baseUrl: str
    :return: Url of sitemap or empty string
        :rtype: str
    """
    file_names = [
        'sitemap.xml',
        'sitemap.txt',
        'sitemap.php',
        'sitemap_index.xml',
        'sitemap-index.xml',
        'sitemap.xml.gz',
        'robots.txt'
    ]

    for file in file_names:
        url = base_url + file
        if is_url(url) and is_valid_url(url):
            return url
    return ''
