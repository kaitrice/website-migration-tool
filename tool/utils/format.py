"""
Format variables.
"""

from urllib.parse import urlparse


def format_url(url: str) -> str:
    """
    Ensure url is base url
    
    :param url: Valid url
        :type url: str
    :return: Base url
        :rtype: str
    """
    parsed_url = urlparse(url)
    if not (parsed_url.scheme and parsed_url.netloc):
        return ""
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
    return base_url
