import validators

def is_url(url_str: str) -> bool:
    return bool(validators.url(url_str))