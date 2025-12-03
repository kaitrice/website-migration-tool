"""Validate input values."""
import validators

def is_url(url_str: str) -> bool:
    """
    Validates url string.
    
    :param url_str: User input of a url.
        :type url_str: str

    :return: Whether the input is a valid string.
        :rtype: bool
    """
    is_valid = validators.url(url_str)
    return bool(is_valid)
