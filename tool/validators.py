"""
Validate input values.
"""
import request
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

def is_valid_url(url_str: str) -> bool:
    """
    Checks if a url is live.
    
    :param url_str: Valid url string
        :type url_str: str
    :return: Whether the url received a successful response code
        :rtype: bool
    """
    try:
        response = request.get(url_str, timeout=5)
        if response.status_code == 200:
            return True
        return False
    except request.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False
